# day_04 — Code Review (Nivel Día 4)

**Herramientas detectadas:** random, random API

## Resumen ejecutivo
- **Correctness:** verificado a simple vista; revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black)*.
- **Robustez:** maneja errores explícitos cuando interactúe con `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Hallazgos
### Docstrings (pydocstyle)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:1 at module level:
-         D100: Missing docstring in public module
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:13 in public function `ascii_print`:
-         D103: Missing docstring in public function
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:51 in public function `win_condition`:
-         D103: Missing docstring in public function
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:59 in public function `normalize_num`:
-         D103: Missing docstring in public function

### Complejidad (Radon)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:13 CC=5 (function) ascii_print
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:51 CC=3 (function) win_condition
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:59 CC=1 (function) normalize_num

## Recomendaciones niveladas
1. Normaliza la entrada con `.strip()` y considera `.lower()`.
2. Evita `while True` sin salida clara; añade condición o `break`.

## Refactor propuesto (acorde al nivel)
- Divide en funciones pequeñas con nombres verbales (`parse_input`, `main`).
- Usa f-strings cuando presentes resultados (https://docs.python.org/3/reference/lexical_analysis.html#f-strings).
- Añade validación suave de entradas (`.strip().lower()`).

## Próximos pasos
- Re-ejecuta tras aplicar formato y correcciones de estilo.
- Cubre al menos 2 casos borde (entrada vacía / valor inesperado).
- Revisa PEP 8: https://peps.python.org/pep-0008/
