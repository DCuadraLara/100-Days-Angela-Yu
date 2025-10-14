# day_01 — Code Review (Nivel Día 1)

## Resumen ejecutivo
- **Correctness:** revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black/Isort)*.
- **Robustez:** maneja errores explícitos cuando haya `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Hallazgos
### Docstrings (pydocstyle)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_01/Project_BandNameGenerator.py:1 at module level:
-         D100: Missing docstring in public module

## Recomendaciones niveladas
1. Normaliza la entrada con `.strip()` y considera `.lower()`.

## Correcciones sugeridas (diffs no destructivos)
```diff
No hay diffs propuestos
```
## Explicación de reglas detectadas
- **D100** ×1 — Añade docstring al módulo (propósito general).

## Tipado estático (mypy)
```text
Success: no issues found in 1 source file

```
## Seguridad (Bandit)
```text
n/a
```
## Mantenibilidad (Radon MI)
```text
/home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_01/Project_BandNameGenerator.py - A (100.00)

```