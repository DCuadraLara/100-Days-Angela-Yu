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

# Explicaciones compactas por código/regla
RULE_EXPLAIN = {
    "E501": "Línea demasiado larga: parte la expresión o extrae lógica.",
    "E302": "Añade líneas en blanco entre definiciones (PEP8).",
    "E303": "Exceso de líneas en blanco: reduce a lo recomendado.",
    "W291": "Espacios al final de línea: elimínalos.",
    "F401": "Import sin usar: elimínalo.",
    "F841": "Variable asignada y no usada.",
    "D100": "Añade docstring al módulo (propósito general).",
    "D101": "Docstring de clase: responsabilidad y uso.",
    "D102": "Docstring de método/función: params y retorno.",
    "D103": "Docstring para funciones a nivel de módulo.",
    "D401": "La primera línea del docstring debe ser una frase en imperativo.",
    "I001": "Ordena imports (isort).",
    "ANN":  "Añade anotaciones de tipo (param/retorno).",
    "UP":   "Actualiza a sintaxis moderna (pyupgrade/ruff).",
    "S":    "Posible riesgo de seguridad (Bandit).",
}

# ---------- utilidades ----------
def run(cmd: str, cwd: Path = REPO_ROOT) -> tuple[int,str,str]:
    p = subprocess.Popen(cmd, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate()
    return p.returncode, out, err

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
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    code, out, _ = run(f'git log --since="{since} 00:00" --name-only --pretty=format:')
    files = sorted({f.strip() for f in out.splitlines() if f.strip()})
    changed = [REPO_ROOT / f for f in files if (REPO_ROOT / f).exists()]
    if changed:
        return changed
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
    code, out, err = run(f"ruff check --output-format=json {' '.join(shlex.quote(str(p)) for p in paths)}")
    issues = []
    if out.strip():
        try:
            issues = json.loads(out)
        except Exception:
            pass
    return issues

def ruff_diff(paths):
    # Correcciones sugeridas sin tocar archivos
    # exit-zero garantiza diffs aunque no falle el exit code
    _, out, _ = run(f"ruff check --fix --diff --exit-zero {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def black_diff(paths):
    _, out, _ = run(f"black --check --diff {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def isort_diff(paths):
    _, out, _ = run(f"isort --check-only --diff {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def radon_cc(paths):
    code, out, err = run(f"radon cc -s -j {' '.join(shlex.quote(str(p)) for p in paths)}")
    try:
        return json.loads(out) if out.strip() else {}
    except Exception:
        return {}

def radon_mi(paths):
    _, out, _ = run(f"radon mi -s {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def pydocstyle_issues(paths):
    _, out, _ = run(f"pydocstyle {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def mypy_check(paths):
    _, out, _ = run(f"mypy --ignore-missing-imports {' '.join(shlex.quote(str(p)) for p in paths)}")
    return out

def bandit_check(paths):
    _, out, _ = run(f"bandit -r {' '.join(shlex.quote(str(p)) for p in paths)} -q")
    return out

def gate_by_level(day:int|None, suggestion:str, level_rules:dict) -> bool:
    avoid = " ".join(level_rules.get("avoid", []))
    tokens = { "list comprehension":"comprehensions","decorator":"decorators","context manager":"context","typing":"typing","generator":"generators" }
    return not any(t in avoid for t in tokens.values())

def count_rules_from_ruff_json(ruff_items):
    counts = Counter()
    for it in ruff_items:
        code = it.get("code")
        if code:
            counts[code] += 1
    return counts

def explain_rules(rule_counts: Counter):
    lines = []
    for code, cnt in rule_counts.most_common():
        base = next((k for k in RULE_EXPLAIN if code.startswith(k)), None)
        msg = RULE_EXPLAIN.get(base or code, "Revisa estilo/seguridad relacionado con la regla.")
        lines.append(f"- **{code}** ×{cnt} — {msg}")
    return "\n".join(lines) if lines else "_Sin hallazgos destacables_."

# ---------- reporte ----------
def make_report(ex_dir: Path, files, global_rules):
    py_files = [f for f in files if f.suffix == ".py"]
    if not py_files:
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
        level_rules
