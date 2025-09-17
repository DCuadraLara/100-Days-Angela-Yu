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
    since = (datetime.datetime.utcnow() - datetime.timedelta

