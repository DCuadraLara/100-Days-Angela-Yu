# tools/reviewer.py
import os, re, json, yaml, datetime, subprocess, shlex
from pathlib import Path
from collections import defaultdict, Counter

REPO_ROOT = Path(__file__).resolve().parents[1]
EXER_DIR   = REPO_ROOT / "exercises"
REPORT_DIR = REPO_ROOT / "reports"
PDF_DIR    = REPO_ROOT / "pdf_report_weekly"
RULES_FILE = REPO_ROOT / "tools" / "rules" / "global.json"
SUMMARY_FILE = REPORT_DIR / "_last_run_exercises.txt"

REPORT_DIR.mkdir(exist_ok=True, parents=True)
PDF_DIR.mkdir(exist_ok=True, parents=True)

MOTIVATION = [
    "La constancia gana a la motivación.",
    "Pequeños pasos diarios, grandes saltos mañana.",
    "Lee el error, entiende la causa, celebra la solución.",
    "Primero que funcione, luego que sea bonito, luego que sea rápido."
]

DOCS = {
    "pep8": "https://peps.python.org/pep-0008/",
    "fstrings": "https://docs.python.org/3/reference/lexical_analysis.html#f-strings",
    "with": "https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects",
    "exceptions": "https://docs.python.org/3/tutorial/errors.html",
    "functions": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
}

# ---------- utilidades ----------
def run(cmd: str, cwd: Path = REPO_ROOT) -> tuple[int,str,str]:
    p = subprocess.Popen(cmd, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate()
    return p.returncode, out, err

def load_global_rules():
    if RULES_FILE.exists():
        # claves numéricas (día) -> dict de reglas
        return {int(k): v for k, v in json.loads(RULES_FILE.read_text(encoding="utf-8")).items()}
    return {}

def load_meta(ex_dir: Path):
    meta = ex_dir / "meta.yml"
    if meta.exists():
        return yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
    return {}

def git_changed_files(days=7):
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    code, out, _ = run(f'git log --since="{since} 00:00" --name-only --pretty=format:')
    files = sorted({f.strip() for f in out.splitlines() if f.strip()})
    changed = [REPO_ROOT / f for f in files if (REPO_ROOT / f).exists()]
    if changed:
        return changed
    # fallback: último commit que tocó exercises/**
    code, out, _ = run('git show --name-only --pretty=format: HEAD -- "exercises/**"')
    return [REPO_ROOT / f for f in out.splitlines() if f.startswith("exercises/") and (REPO_ROOT / f).exists()]

def infer_day_from_path(p: Path):
    m = re.search(r"day[_-]?(\d+)", str(p).lower())
    return int(m.group(1)) if m else None

def detect_tools(py_code: str):
    tools = set()
    if re.search(r"\bimport\s+random\b", py_code): tools.add("random")
    if re.search(r"\bimport\s+math\b", py_code): tools.add("math")
    if re.search(r"\bimport\s+re\b", py_code): tools.add("re")
    if re.search(r"\bimport\s+time\b", py_code): tools.add("time")
    if re.search(r"\bimport\s+os\b", py_code) or "os." in py_code: tools.add("os")
    if re.search(r"\brequests\b", py_code): tools.add("requests")
    if re.search(r"\bopen\s*\(", py_code): tools.add("file I/O")
    if "random." in py_code: tools.add("random API")
    return tools

def check_forbidden(py_code: str, forbidden_rules):
    hits = []
    for rule in forbidden_rules or []:
        pat = rule.split("#", 1)[0].strip()
        if not pat: continue
        try:
            if re.search(pat, py_code): hits.append(rule)
        except re.error:
            if pat in py_code: hits.append(rule)
    return hits

def tips_for_level(py_code: str, level_rules: dict):
    tips = []
    allowed = " ".join(level_rules.get("allowed", []))
    if ("print(" in py_code) and ("f\"" not in py_code and "f'" not in py_code) and ("f-strings" in allowed):
        tips.append("Usa f-strings para salidas claras (PEP 498).")
    if "input(" in py_code and not re.search(r"\.strip\(\)", py_code):
        tips.append("Normaliza la entrada con `.strip()` y considera `.lower()`.")
    if re.search(r"while\s+True\s*:", py_code) and "while True" not in allowed:
        tips.append("Evita `while True` sin salida clara; añade condición o `break`.")
    return tips

def collect_exercises(changed_paths):
    grouped = defaultdict(list)
    for p in changed_paths:
        if str(EXER_DIR) not in str(p): continue
        for q in p.parents:
            if q.parent == EXER_DIR:
                grouped[q].append(p); break
    return grouped

# ---------- análisis profesional ----------
def ruff_lint(paths):
    # Devolvemos issues en formato parseable
    code, out, err = run(f"ruff check --output-format=json {' '.join(shlex.quote(str(p)) for p in paths)}")
    issues = []
    if out.strip():
        try:
            import json as _json
            issues = _json.loads(out)
        except Exception:
            pass
    return issues

def black_diff(paths):
    # Modo check y diff para sugerir formato
    code, out, err = run(f"black --check --diff {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def radon_cc(paths):
    # Complejidad ciclomática
    code, out, err = run(f"radon cc -s -j {' '.join(shlex.quote(str(p)) for p in paths)}")
    try:
        import json as _json
        return _json.loads(out) if out.strip() else {}
    except Exception:
        return {}

def pydocstyle_issues(paths):
    code, out, err = run(f"pydocstyle {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def gate_by_level(day:int|None, suggestion:str, level_rules:dict) -> bool:
    """Filtra sugerencias demasiado avanzadas para el día actual."""
    avoid = " ".join(level_rules.get("avoid", []))
    # heurística simple: si la clave aparece en avoid, no proponer
    tokens = {
        "list comprehension":"comprehensions",
        "decorator":"decorators",
        "context manager":"context",
        "typing":"typing",
        "generator":"generators",
    }
    return not any(t in avoid for t in tokens.values())

# ---------- reporte ----------
def make_report(ex_dir: Path, files, global_rules):
    py_files = [f for f in files if f.suffix == ".py"]
    if not py_files:
        # Si solo cambiaron README, generar una nota mínima
        title = ex_dir.name
        report_path = REPORT_DIR / f"{ex_dir.name}_report.md"
        report_path.write_text(f"# {title} — Report\n\nSolo se detectaron cambios no-Python.\n", encoding="utf-8")
        return report_path, {"title": title, "tips": [], "tools": []}

    day = None
    for f in files:
        day = infer_day_from_path(f) or day

    level_rules = global_rules.get(day, {})
    overrides = load_meta(ex_dir)
    if overrides.get("day"):
        day = overrides["day"]
        level_rules = global_rules.get(day, level_rules)

    forbidden = (overrides.get("forbidden") or [])
    must_cover = (overrides.get("must_cover") or [])
    tips_extra = (overrides.get("tips_extra") or [])

    # Leer códigos
    code_by_file, tools, forbidden_hits, tips = {}, set(), [], []
    for f in py_files:
        code = f.read_text(encoding="utf-8", errors="ignore")
        code_by_file[f] = code
        tools |= detect_tools(code)
        forbidden_hits.extend(check_forbidden(code, forbidden))
        tips.extend(tips_for_level(code, level_rules))

    # Linters / análisis
    ruff = ruff_lint(py_files)
    black_changes = black_diff(py_files)
    radon = radon_cc(py_files)
    pyds = pydocstyle_issues(py_files)

    # Curación de issues (texto legible)
    style_issues = []
    for item in ruff:
        msg = f"{item.get('filename')}:{item.get('location',{}).get('row')}:{item.get('location',{}).get('column')} {item.get('code')} {item.get('message')}"
        if gate_by_level(day, msg, level_rules):
            style_issues.append(msg)

    doc_issues = [l for l in pyds.splitlines() if l.strip()]

    complexity_rows = []
    for file, entries in (radon or {}).items():
        for e in entries:
            complexity_rows.append(f"{file}:{e.get('lineno')} CC={e.get('complexity')} ({e.get('type')}) {e.get('name')}")

    # Unificar tips
    def uniq(seq): return list(dict.fromkeys(seq))
    tips = uniq(tips + tips_extra)

    # Título
    title = overrides.get("title") or ex_dir.name

    # Construir Markdown robusto
    md = []
    md.append(f"# {title} — Code Review (Nivel Día {day if day else 'N/A'})\n")
    if tools:
        md.append(f"**Herramientas detectadas:** {', '.join(sorted(tools))}\n")
    if must_cover:
        md.append(f"**Debe cubrir:** {'; '.join(must_cover)}\n")
    if forbidden:
        md.append(f"**Evitar (según nivel):** {'; '.join(forbidden)}\n")

    md.append("## Resumen ejecutivo")
    md.append("- **Correctness:** verificado a simple vista; revisar entradas/salidas y casos borde.")
    md.append("- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black)*.")
    md.append("- **Robustez:** maneja errores explícitos cuando interactúe con `input()` o archivos.")
    md.append("- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.")
    md.append("")

    if style_issues or "diff" in black_changes or doc_issues or complexity_rows:
        md.append("## Hallazgos")
        if style_issues:
            md.append("### Estilo (Ruff)")
            md.extend([f"- {x}" for x in style_issues[:50]])  # limitar ruido
            md.append(f"_Referencia_: {DOCS['pep8']}\n")
        if black_changes and "reformatted" in black_changes or "would reformat" in black_changes:
            md.append("### Formato (Black — sugerencia)")
            md.append("Se recomienda aplicar Black para formato consistente. (Ejecuta `black exercises/day_xx/`)")
            md.append("")
        if doc_issues:
            md.append("### Docstrings (pydocstyle)")
            md.extend([f"- {x}" for x in doc_issues[:30]])
            md.append("")
        if complexity_rows:
            md.append("### Complejidad (Radon)")
            md.extend([f"- {x}" for x in complexity_rows])
            md.append("")

    if forbidden_hits:
        md.append("## Incumplimientos según nivel")
        md.extend([f"- {x}" for x in forbidden_hits])
        md.append("")

    if tips:
        md.append("## Recomendaciones niveladas")
        for i, t in enumerate(tips, 1):
            md.append(f"{i}. {t}")
        md.append("")

    # Refactor propuesto (light & nivelado)
    md.append("## Refactor propuesto (acorde al nivel)")
    if day and day <= 5:
        md.append("- Divide en funciones pequeñas con nombres verbales (`parse_input`, `main`).")
        md.append(f"- Usa f-strings cuando presentes resultados ({DOCS['fstrings']}).")
        md.append("- Añade validación suave de entradas (`.strip().lower()`).")
    elif day and day <= 10:
        md.append("- Añade docstrings breves (`\"\"\"Qué hace, args, return\"\"\"`).")
        md.append("- Evita `while True` sin condición de salida.")
        md.append("- Aplica `with open(...)` en I/O para cierre automático.")
    else:
        md.append("- Separa lógica del CLI y valora tests mínimos.")
    md.append("")

    md.append("## Próximos pasos")
    md.append("- Re-ejecuta tras aplicar formato y correcciones de estilo.")
    md.append("- Cubre al menos 2 casos borde (entrada vacía / valor inesperado).")
    md.append(f"- Revisa PEP 8: {DOCS['pep8']}")
    md.append("")

    report_path = REPORT_DIR / f"{ex_dir.name}_report.md"
    report_path.write_text("\n".join(md), encoding="utf-8")

    # Para PDF semanal
    return report_path, {
        "title": title,
        "tips": [t for t in tips][:5],
        "tools": sorted(tools)
    }

# ---------- PDF semanal enriquecido ----------
def generate_week_pdf(items):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm

    today = datetime.date.today().isoformat()
    out = PDF_DIR / f"week-{today}.pdf"
    c = canvas.Canvas(str(out), pagesize=A4)
    w, h = A4
    y = h - 2*cm

    def line(txt, dy=14):  # simple writer
        nonlocal y
        c.drawString(2*cm, y, txt)
        y -= dy
        if y < 2*cm:
            c.showPage(); y = h - 2*cm

    line("Resumen semanal — 100 Days of Code", 18)
    line(f"Fecha: {today}", 20)
    line("Ejercicios revisados:", 18)

    counter = Counter()
    for it in items:
        line(f"• {it['title']}", 16)
        for t in it["tips"]:
            line(f"   - {t}", 14)
        for tl in it["tools"]:
            counter[tl] += 1

    if counter:
        line("", 18); line("Herramientas más usadas:", 18)
        for k, v in sorted(counter.items(), key=lambda x: -x[1]):
            line(f"• {k}: {v}", 14)

    line("", 18)
    mot = MOTIVATION[datetime.date.today().isocalendar().week % len(MOTIVATION)]
    line("Motivación: " + mot, 18)
    c.showPage(); c.save()
    return out

# ---------- main ----------
def main():
    global_rules = load_global_rules()
    changed = git_changed_files(7)
    grouped = collect_exercises(changed)

    items, processed_lines = [], []
    today = datetime.date.today().isoformat()

    for ex_dir, files in sorted(grouped.items(), key=lambda x: x[0].name):
        report_path, item = make_report(ex_dir, files, global_rules)
        items.append(item)
        processed_lines.append(f"{item['title']} | {today}")

    if items:
        generate_week_pdf(items)
        print(f"Reports: {len(items)} — PDF generado.")
    else:
        print("No hay ejercicios nuevos esta semana.")

    SUMMARY_FILE.write_text("\n".join(processed_lines) if processed_lines else "No se detectaron ejercicios esta semana.", encoding="utf-8")
    if processed_lines:
        print("Procesados:\n" + "\n".join(processed_lines))

if __name__ == "__main__":
    main()
