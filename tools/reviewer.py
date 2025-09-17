# tools/reviewer.py
import os, re, json, datetime, subprocess
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parents[1]
EXER_DIR   = REPO_ROOT / "exercises"
REPORT_DIR = REPO_ROOT / "reports"
PDF_DIR    = REPO_ROOT / "pdf_report_weekly"
RULES_FILE = REPO_ROOT / "tools" / "review_rules.json"

REPORT_DIR.mkdir(exist_ok=True)
PDF_DIR.mkdir(exist_ok=True)

DEFAULT_RULES = {
    1:  ["input()/print", "variables", "f-strings", "if/else simples"],
    2:  ["operadores", "condicionales anidados", "nombres claros"],
    3:  ["listas", "% módulo", "funciones pequeñas"],
    4:  ["diccionarios/sets básicos", "for/while"],
    5:  ["funciones con return", "docstrings cortos"],
    6:  ["try/except sencillo", "validación de input"],
    7:  ["list comprehensions (intro)"],
    8:  ["I/O de archivos (intro)"],
    9:  ["módulos e imports básicos"],
    10: ["estructura mínima de proyecto"]
}

MOTIVATION = [
    "La constancia gana a la motivación.",
    "Pequeños pasos diarios, grandes saltos mañana.",
    "Lee el error, entiende la causa, celebra la solución.",
    "Primero que funcione, luego que sea bonito, luego que sea rápido."
]

def load_rules():
    if RULES_FILE.exists():
        try:
            data = json.loads(RULES_FILE.read_text(encoding="utf-8"))
            return {int(k): v for k, v in data.items()}
        except Exception:
            pass
    return DEFAULT_RULES

def git_changed_files(days=7):
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    cmd = ["git", "log", f'--since="{since} 00:00"', "--name-only", "--pretty=format:"]
    out = subprocess.check_output(" ".join(cmd), shell=True, cwd=REPO_ROOT).decode("utf-8", "ignore")
    files = sorted({f.strip() for f in out.splitlines() if f.strip()})
    return [REPO_ROOT / f for f in files if (REPO_ROOT / f).exists()]

def infer_day_from_path(p: Path):
    m = re.search(r"day[_-]?(\d+)", str(p).lower())
    return int(m.group(1)) if m else None

def detect_tools(py_code: str):
    tools = set()
    # heurísticas simples
    if re.search(r"\bimport\s+random\b", py_code): tools.add("random")
    if re.search(r"\bimport\s+math\b", py_code): tools.add("math")
    if re.search(r"\bimport\s+re\b", py_code): tools.add("re")
    if re.search(r"\bopen\s*\(", py_code): tools.add("file I/O")
    if re.search(r"\brequests\b", py_code): tools.add("requests")
    return tools

def lint_tips(py_code: str, day: int, rules: dict):
    tips = []
    day_rules = rules.get(day, [])
    if day_rules:
        tips.append(f"**Enfoque Día {day}:** " + ", ".join(day_rules))

    # aconsejar acorde al nivel (suave)
    if ("print(" in py_code) and ("f\"" not in py_code and "f'" not in py_code) and day >= 1:
        tips.append("Usa f-strings para salidas claras (si ya están vistas en este día).")
    if "input(" in py_code and not re.search(r"\.strip\(\)", py_code):
        tips.append("Aplica `.strip()` al `input()` para evitar espacios accidentales.")
    if re.search(r"while\s+True\s*:", py_code) and "break" not in py_code:
        tips.append("Evita bucles infinitos sin condición/salida clara; añade un `break` o condición.")
    if re.search(r"if\s+.+:\s*\n\s*pass", py_code):
        tips.append("Evita `pass` en ramas importantes; completa la lógica o elimina la rama.")
    if len(py_code.splitlines()) > 150:
        tips.append("Divide en funciones pequeñas para mejorar legibilidad y pruebas.")
    return list(dict.fromkeys(tips))

def collect_exercise_units(changed_paths):
    grouped = defaultdict(list)
    for p in changed_paths:
        if str(EXER_DIR) not in str(p): 
            continue
        # agrupa por carpeta de ejercicio (day_xx)
        for q in p.parents:
            if q.parent == EXER_DIR:
                grouped[q.name].append(p)
                break
    return grouped

def make_report(ex_name: str, day: int, files, rules):
    tips, tools = [], set()
    for f in files:
        if f.suffix == ".py":
            code = f.read_text(encoding="utf-8", errors="ignore")
            tips.extend(lint_tips(code, day, rules))
            tools |= detect_tools(code)
    tips = list(dict.fromkeys(tips)) or ["Código correcto para el nivel. ¡Sigue así!"]

    md = []
    md.append(f"# {ex_name} — Report\n")
    md.append(f"**Día detectado:** {day if day else 'N/A'}")
    if tools:
        md.append(f"**Herramientas vistas:** {', '.join(sorted(tools))}")
    md.append("\n## Revisión y mejoras propuestas\n")
    for i, tip in enumerate(tips, 1):
        md.append(f"{i}. {tip}")
    md.append("\n## Siguientes pasos (acorde al nivel)\n")
    if day and day < 5:
        md.append("- Añade validación básica de entrada y mensajes de error claros.")
    elif day and day < 9:
        md.append("- Separa lógica en funciones y añade docstrings breves.")
    else:
        md.append("- Considera tests mínimos (inputs típicos y casos borde).")
    md.append("\n## Snippet orientativo (si aplica)\n")
    md.append("> Incluye aquí un mini refactor acorde al día (opcional).")
    out = REPORT_DIR / f"{ex_name}_report.md"
    out.write_text("\n".join(md), encoding="utf-8")
    return out, tools

def generate_week_pdf(summary):
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
    tool_counter = defaultdict(int)

    for ex_name, tips, tools in summary:
        line(f"• {ex_name}", 16)
        for t in tips[:5]:
            line(f"   - {t}", 14)
        for tl in tools:
            tool_counter[tl] += 1

    if tool_counter:
        line("", 18)
        line("Herramientas más usadas:", 18)
        for k, v in sorted(tool_counter.items(), key=lambda x: -x[1]):
            line(f"• {k}: {v} ejercicios", 14)

    line("", 18)
    line("Tip de la semana: " + MOTIVATION[datetime.date.today().isocalendar().week % len(MOTIVATION)], 18)
    c.showPage()
    c.save()
    return out

def main():
    rules = load_rules()
    changed = git_changed_files(7)
    grouped = collect_exercise_units(changed)

    summary = []
    for ex, files in sorted(grouped.items()):
        day = None
        for f in files:
            day = infer_day_from_path(f) or day
        report_path, tools = make_report(ex, day, files, rules)
        # extrae tips del report para el PDF
        tips = []
        for line in report_path.read_text(encoding="utf-8").splitlines():
            if re.match(r"\d+\.\s", line):
                tips.append(re.sub(r"^\d+\.\s", "", line))
        summary.append((ex, tips, tools))

    if summary:
        pdf_path = generate_week_pdf(summary)
        print(f"Generated {len(summary)} reports and PDF: {pdf_path}")
    else:
        print("No new exercises this week.")

if __name__ == "__main__":
    main()

