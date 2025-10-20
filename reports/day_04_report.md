# day_04 — Code Review (Nivel Día 4)

**Herramientas detectadas:** random, random API

## Resumen ejecutivo
- **Correctness:** revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black/Isort)*.
- **Robustez:** maneja errores explícitos cuando haya `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Hallazgos
### Docstrings (pydocstyle)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:1 at module level:
-         D100: Missing docstring in public module
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:8 in public function `ascii_print`:
-         D103: Missing docstring in public function
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:56 in public function `win_condition`:
-         D103: Missing docstring in public function
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:65 in public function `normalize_num`:
-         D103: Missing docstring in public function

### Complejidad (Radon)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:8 CC=5 (function) ascii_print
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:56 CC=3 (function) win_condition
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:65 CC=1 (function) normalize_num

## Recomendaciones niveladas
1. Normaliza la entrada con `.strip()` y considera `.lower()`.
2. Evita `while True` sin salida clara; añade condición o `break`.

## Correcciones sugeridas (diffs no destructivos)
```diff
# Ruff
--- exercises/day_04/RockPaperScissors.py
+++ exercises/day_04/RockPaperScissors.py
@@ -174,7 +174,7 @@
                 )
 
                 if player_1 in (1, 2, 3) and player_2 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
-                    
+
                     print("----------------------------")
                     print("\nThe player 1 hero hand is... \n")
                     player_1 = normalize_num(player_1)

Would fix 1 error (6 additional fixes available with `--unsafe-fixes`).

# Black
--- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py	2025-10-20 05:17:02.777801+00:00
+++ /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py	2025-10-20 05:17:16.777300+00:00
@@ -1,6 +1,5 @@
-
 # Rock Paper Scissors game with a creative touch, here you have 3 modes normal - hard - Vsplayer.
 
 import random
 
 
@@ -50,11 +49,10 @@
                                         `/          """
         '''
         )
 
 
-
 def win_condition(player, ia):
     if player == ia:
         return "--- DRAW ---"
     elif (player - ia) % 3 == 1:
         return "--- PLAYER WINS ---"
@@ -171,12 +169,16 @@
                     input(
                         "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
                     )
                 )
 
-                if player_1 in (1, 2, 3) and player_2 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
-                    
+                if player_1 in (1, 2, 3) and player_2 in (
+                    1,
+                    2,
+                    3,
+                ):  # Check player hand as a valid answer to break Loop.
+
                     print("----------------------------")
                     print("\nThe player 1 hero hand is... \n")
                     player_1 = normalize_num(player_1)
                     ascii_print(player_1)
                     print("The player 2 hero hand is... \n")

```
## Explicación de reglas detectadas
- **E501** ×5 — Línea demasiado larga: parte la expresión o extrae lógica.
- **ANN001** ×4 — Añade anotaciones de tipo (param/retorno).
- **W291** ×4 — Espacios al final de línea: elimínalos.
- **ANN201** ×3 — Añade anotaciones de tipo (param/retorno).
- **D103** ×3 — Docstring para funciones a nivel de módulo.
- **S311** ×2 — Posible riesgo de seguridad (Bandit).
- **D100** ×1 — Añade docstring al módulo (propósito general).
- **W293** ×1 — Revisa estilo/seguridad relacionado con la regla.

## Tipado estático (mypy)
```text
Success: no issues found in 1 source file

```
## Seguridad (Bandit)
```text
Run started:2025-10-20 05:17:17.647252

Test results:
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_calls.html#b311-random
   Location: /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:108:22
107	            # IA roll for a random hand.
108	            ia_hand = random.randint(0, 2)
109	

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_calls.html#b311-random
   Location: /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:139:22
138	            choice_list.append("Shotgun")
139	            ia_hand = random.randint(0, 3)
140	

--------------------------------------------------

Code scanned:
	Total lines of code: 156
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 2
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 2
Files skipped (0):

```
## Mantenibilidad (Radon MI)
```text
/home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py - A (51.69)

```