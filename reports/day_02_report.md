# day_02 — Code Review (Nivel Día 2)

## Resumen ejecutivo
- **Correctness:** revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black/Isort)*.
- **Robustez:** maneja errores explícitos cuando haya `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Recomendaciones niveladas
1. Normaliza la entrada con `.strip()` y considera `.lower()`.

## Correcciones sugeridas (diffs no destructivos)
```diff
# Black
--- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_02/tip_calculator.py	2025-10-15 09:57:24.222692+00:00
+++ /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_02/tip_calculator.py	2025-10-15 09:57:35.588614+00:00
@@ -5,6 +5,6 @@
 
 print("Welcome to the tip calculator!")
 people = int(input("Number of people: "))
 split_bill = (bill / people) * 1.12
 
-print(f"Each person should pay:{split_bill:.2f} Dollars") # split_bill:2f shows 2 decimates.
+print(f"Each person should pay:{split_bill:.2f} Dollars")  # split_bill:2f shows 2 decimates.

```
## Explicación de reglas detectadas
_Sin hallazgos destacables_.

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
/home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_02/tip_calculator.py - A (100.00)

```