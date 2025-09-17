# tools/reviewer.py
import os, re, json, yaml, datetime, subprocess
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parents[1]
EXER_DIR   = REPO_ROOT / "exercises"
REPORT_DIR = REPO_ROOT / "reports"
PDF_DIR    = REPO_ROOT / "pdf_report_weekly"
RULES_FILE = REPO_ROOT / "tools" / "rules" / "global.json"

REPORT_DIR.mkdir(exist_ok=True, parents=True)
PDF_DIR.mkdir(exist_ok=True, parents=True)

MOTIVATION = [
    "La constancia gana a la motivación.",
    "Pequeños pasos diarios, grandes saltos mañana.",
    "Lee el error, entiende la causa, celebra la solución.",
    "Primero que funcione, luego que sea bonito, luego que sea rápido."
]

def load_global_rules():
    if RULES_FILE.exists():
        return {int(k): v for k, v in json.loads(RULES_FILE.read_text(encoding="utf-8")).items()}
    return {}

def load_meta(ex_dir: Path):
    meta = ex_dir / "meta.yml"
    if meta.exists():
        return yaml.safe_load(meta.read_text(encoding="utf-8")) or {}
    return {}

def git_changed_files(days=7):
    """
    Devuelve archivos cambiados en los últimos `days` días.
    Incluye fallback al último commit en exercises/** si no hay cambios recientes
    (útil en el primer run o con fetch-depth bajo).
    """
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    cmd = ["git", "log", f'--since="{since} 00:00"', "--name-only", "--pretty=format:"]
    try:
        out = subprocess.check_output(" ".join(cmd), shell=True, cwd=REPO_ROOT).decode("utf-8", "ignore")
    except subprocess.CalledProcessError:
        out = ""
    files = sorted({f.strip() for f in out.splitlines() if f.strip()})
    changed = [REPO_ROOT / f for f in files if (REPO_ROOT / f).exists()]

    if changed:
        return changed

    # Fallback: tomar archivos tocados en exercises/** del último commit
    try:
        out = subprocess.check_output(
            'git show --name-only --pretty=format: HEAD -- "exercises/**"',
            shell=True, cwd=REPO_ROOT
        ).decode("utf-8", "ignore")
        fallback = [REPO_ROOT / f for f in out.splitlines() if f.startswith("exercises/") and (REPO_ROOT / f).exists()]
        if fallback:
            return fallback
    except Exception:
        pass

    return []

def infer_day_from_path(p: Path):
    m = re.search(r"day[_-]?(\d+)", str(p).lower())
    return int(m.group(1)) if m else None

def detect_tools(py_code: str):
    tools = set()
    # imports y usos típicos de primeros días
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
        if not pat:
            continue
        try:
            if re.search(pat, py_code):
                hits.append(rule)
        except re.error:
            if pat in py_code:
                hits.append(rule)
    return hits

def tips_for_level(py_code: str, level_rules: dict):
    tips = []
    allowed = " ".join(level_rules.get("allowed", []))

    # Consejos suaves alineados al nivel
    if ("print(" in py_code) and ("f\"" not in py_code and "f'" not in py_code) and ("f-strings" in allowed):
        tips.append("Usa f-strings para salidas claras.")
    if "input(" in py_code and not re.search(r"\.strip\(\)", py_code):
        tips.append("Normaliza la entrada con `.strip()` (y `.lower()` si procede).")
    if re.search(r"while\s+True\s*:", py_code) and "while True" not in allowed:
        tips.append("Evita `while True` sin salida clara; añade condición o `break`.")

    return tips

def collect_exercises(changed_paths):
    grouped = defaultdict(list)
    for p in changed_paths:
        if str(EXER_DIR) not in str(p):
            continue
        # agrupar por carpeta inmediata bajo exercises/
        for q in p.parents:
            if q.parent == EXER_DIR:
                grouped[q].append(p)
                break
    return grouped

def make_report(ex_dir: Path, files, global_rules):
    # día detectado
    day = None
    for f in files:
        day = infer_day_from_path(f) or day

    level_rules = global_rules.get(day, {})
    overrides = load_meta(ex_dir)  # title, day, must_cover, forbidden, tips_extra...
    if overrides.get("day"):
        day = overrides["day"]
        level_rules = global_rules.get(day, level_rules)

    # fusiona
    forbidden = (overrides.get("forbidden") or [])
    must_cover = (overrides.get("must_cover") or [])
    tips_extra = (overrides.get("tips_extra") or [])

    tips, tools = [], set()
    forbidden_hits = []
    for f in files:
        if f.suffix == ".py":
            code = f.read_text(encoding="utf-8", errors="ignore")
            tips.extend(tips_for_level(code, level_rules))
            tools |= detect_tools(code)
            forbidden_hits.extend(check_forbidden(code, forbidden))

    # de-duplicar
    def uniq(seq): return list(dict.fromkeys(seq))
    tips = uniq(tips + tips_extra)
    forbidden_hits = uniq(forbidden_hits)

    title = overrides.get("title") or ex_dir.name
    out_md = [f"# {title} — Report", ""]
    out_md.append(f"**Día (nivel) detectado:** {day if day else 'N/A'}")
    if tools:
        out_md.append(f"**Herramientas vistas:** {', '.join(sorted(tools))}")
    if must_cover:
        out_md.append("**Debe cubrir:** " + "; ".join(must_cover))
    if forbidden:
        out_md.append("**Evitar:** " + "; ".join(forbidden))

    out_md.append("\n## Revisión y mejoras propuestas")
    if tips:
        for i, t in enumerate(tips, 1):
            out_md.append(f"{i}. {t}")
    else:
        out_md.append("- Código correcto para el nivel. ¡Sigue así!")

    if forbidden_hits:
        out_md.append("\n## Hallazgos a corregir (prohibidos en este nivel)")
        for h in forbidden_hits:
            out_md.append(f"- {h}")

    out_md.append("\n## Siguientes pasos (acorde al nivel)")
    if day and day < 5:
        out_md.append("- Valida inputs y divide en funciones pequeñas.")
    elif day and day < 9:
        out_md.append("- Añade docstrings breves y pruebas manuales simples.")
    else:
        out_md.append("- Considera tests mínimos y separar lógica/CLI.")

    report_path = REPORT_DIR / f"{ex_dir.name}_report.md"
    report_path.write_text("\n".join(out_md), encoding="utf-8")

    # datos para el PDF
    return report_path, {
        "title": title,
        "tips": [t for t in tips][:5],
        "tools": sorted(tools)
    }

def generate_week_pdf(items):
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import cm

    today = datetime.date.today().isoformat()
    out = PDF_DIR / f"week-{today}.pdf"
    c = canvas.Canvas(str(out), pagesize=A4)
    w, h = A4
    y = h - 2*cm

    def line(txt, dy=14):
        nonlocal y
        c.drawString(2*cm, y, txt)
        y -= dy
        if y < 2*cm:
            c.showPage()
            y = h - 2*cm

    line("Resumen semanal — 100 Days of Code")
    line(f"Fecha: {today}", 20)
    line("Ejercicios revisados:", 18)
    counter = defaultdict(int)

    for it in items:
        line(f"• {it['title']}", 16)
        for t in it["tips"]:
            line(f"   - {t}", 14)
        for tl in it["tools"]:
            counter[tl] += 1

    if counter:
        line("", 18)
        line("Herramientas más usadas:", 18)
        for k, v in sorted(counter.items(), key=lambda x: -x[1]):
            line(f"• {k}: {v}", 14)

    line("", 18)
    line("Motivación: " + MOTIVATION[datetime.date.today().isocalendar().week % len(MOTIVATION)], 18)
    c.showPage()
    c.save()
    return out

def main():
    global_rules = load_global_rules()
    changed = git_changed_files(7)
    grouped = collect_exercises(changed)

    items = []
    for ex_dir, files in sorted(grouped.items(), key=lambda x: x[0].name):
        report_path, item = make_report(ex_dir, files, global_rules)
        items.append(item)

    if items:
        generate_week_pdf(items)
        print(f"Reports: {len(items)} — PDF generado.")
    else:
        print("No hay ejercicios nuevos esta semana.")

if __name__ == "__main__":
    main()
