# day_03 — Code Review (Nivel Día 3)

## Resumen ejecutivo
- **Correctness:** verificado a simple vista; revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black)*.
- **Robustez:** maneja errores explícitos cuando interactúe con `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Hallazgos
### Docstrings (pydocstyle)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:1 at module level:
-         D205: 1 blank line required between summary line and description (found 0)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:1 at module level:
-         D209: Multi-line docstring closing quotes should be on a separate line
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:78 in public function `reset_player`:
-         D103: Missing docstring in public function

### Complejidad (Radon)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:78 CC=1 (function) reset_player

## Refactor propuesto (acorde al nivel)
- Divide en funciones pequeñas con nombres verbales (`parse_input`, `main`).
- Usa f-strings cuando presentes resultados (https://docs.python.org/3/reference/lexical_analysis.html#f-strings).
- Añade validación suave de entradas (`.strip().lower()`).

## Próximos pasos
- Re-ejecuta tras aplicar formato y correcciones de estilo.
- Cubre al menos 2 casos borde (entrada vacía / valor inesperado).
- Revisa PEP 8: https://peps.python.org/pep-0008/
