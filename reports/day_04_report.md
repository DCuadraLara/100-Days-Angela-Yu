# day_04 — Code Review (Nivel Día 4)

**Herramientas detectadas:** random, random API

## Resumen ejecutivo
- **Correctness:** revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black/Isort)*.
- **Robustez:** maneja errores explícitos cuando haya `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Hallazgos
### Orden de imports (isort — sugerencia)
Se recomienda ordenar imports para coherencia.

### Docstrings (pydocstyle)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:1 at module level:
-         D100: Missing docstring in public module
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:7 in public function `ascii_print`:
-         D103: Missing docstring in public function
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:45 in public function `win_condition`:
-         D103: Missing docstring in public function
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:54 in public function `normalize_num`:
-         D103: Missing docstring in public function

### Complejidad (Radon)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:7 CC=5 (function) ascii_print
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:45 CC=3 (function) win_condition
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:54 CC=1 (function) normalize_num

## Recomendaciones niveladas
1. Normaliza la entrada con `.strip()` y considera `.lower()`.
2. Evita `while True` sin salida clara; añade condición o `break`.

## Correcciones sugeridas (diffs no destructivos)
```diff
# Ruff
--- exercises/day_04/RockPaperScissors.py
+++ exercises/day_04/RockPaperScissors.py
@@ -3,6 +3,7 @@
 
 import random
 
+
 # Win condition function.
 def ascii_print(choice_num):
     if choice_num == 0:
@@ -166,9 +167,9 @@
 
             except ValueError:
                 print("Select a correct hero hand!")
-              
+
     except ValueError:
         print("Invalid Mode. Please select again.")
     break
-  
+
 print("\n\nThanks for playing my game :) ")

Would fix 3 errors (6 additional fixes available with `--unsafe-fixes`).

# isort
--- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:before	2025-10-14 18:45:39.482460
+++ /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:after	2025-10-14 18:45:53.370653
@@ -2,6 +2,7 @@
 # Rock Paper Scissors game with a creative touch, here you have 3 modes normal - hard - Vsplayer
 
 import random
+
 
 # Win condition function.
 def ascii_print(choice_num):

# Black
--- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py	2025-10-14 18:45:39.482460+00:00
+++ /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py	2025-10-14 18:45:53.063897+00:00
@@ -1,48 +1,57 @@
-
 # Rock Paper Scissors game with a creative touch, here you have 3 modes normal - hard - Vsplayer
 
 import random
+
 
 # Win condition function.
 def ascii_print(choice_num):
     if choice_num == 0:
-        print('''
+        print(
+            '''
                             _______         
                         ---'   ____)
                               (_____)
                               (_____)
                               (____)
                         ---.__(___)
-                        ''')
+                        '''
+        )
     elif choice_num == 1:
-        print('''
+        print(
+            '''
                             _______         
                         ---'   ____)____
                                   ______)
                                   _______)
                                  _______)
                         ---.__________)
-                     ''')
+                     '''
+        )
     elif choice_num == 2:
-        print('''
+        print(
+            '''
                          _______        
                      ---'   ____)____
                                  ______)
                                __________)
                            (____)
                       ---.__(___)
-                      ''')
+                      '''
+        )
     elif choice_num == 3:
-        print('''
+        print(
+            '''
 ,________________________________       
 |__________,----------._ [____]  ""-,__  __...-----==="
         (_(||||||||||||)___________/   ""             |
            `----------' Krogg98[ ))"-,                |
                                 ""    `,  _,--...___  |
                                         `/          """
-        ''')
+        '''
+        )
+
 
 def win_condition(player, ia):
     if player == ia:
         return "--- DRAW ---"
     elif (player - ia) % 3 == 1:
@@ -80,13 +89,17 @@
         if mode == 1:
             print("\nStarting game...\n")
 
             while True:
                 try:
-                    player_1 = int(input("Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"))
-
-                    if player_1 in (1, 2, 3): # Check player hand as a valid answer to break Loop.
+                    player_1 = int(
+                        input(
+                            "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
+                        )
+                    )
+
+                    if player_1 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
                         player_1 = normalize_num(player_1)
                         break
                 except ValueError:
                     print("Select a correct hero hand!")
 
@@ -98,19 +111,23 @@
             ascii_print(player_1)
             print("The IA villain hand is... \n")
             ascii_print(ia_hand)
 
             print(win_condition(player_1, ia_hand))
-            break # End loop condition.
+            break  # End loop condition.
 
         # 2. -- Hard mode.
         elif mode == 2:
             print("\nStarting game...\n")
 
             while True:
                 try:
-                    player_1 = int(input("Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"))
+                    player_1 = int(
+                        input(
+                            "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
+                        )
+                    )
 
                     if player_1 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
                         player_1 = normalize_num(player_1)
                         break
                 except ValueError:
@@ -140,16 +157,28 @@
 
         while True:
             try:
                 print("Player 1 -- Turn")
                 print("Player 2 dont cheat! Dont look here :D \n")
-                player_1 = int(input("Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"))
+                player_1 = int(
+                    input(
+                        "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
+                    )
+                )
 
                 print("Player 2 - Your turn")
-                player_2 = int(input("Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"))
-
-                if player_1 in (1, 2, 3) and player_2 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
+                player_2 = int(
+                    input(
+                        "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
+                    )
+                )
+
+                if player_1 in (1, 2, 3) and player_2 in (
+                    1,
+                    2,
+                    3,
+                ):  # Check player hand as a valid answer to break Loop.
                     print("----------------------------")
                     print("\nThe player 1 hero hand is... \n")
                     player_1 = normalize_num(player_1)
                     ascii_print(player_1)
                     print("The player 2 hero hand is... \n")
@@ -164,11 +193,11 @@
                         print("--- Player 2 Wins! ---")
                     break
 
             except ValueError:
                 print("Select a correct hero hand!")
-              
+
     except ValueError:
         print("Invalid Mode. Please select again.")
     break
-  
+
 print("\n\nThanks for playing my game :) ")

```
## Explicación de reglas detectadas
- **E501** ×5 — Línea demasiado larga: parte la expresión o extrae lógica.
- **ANN001** ×4 — Añade anotaciones de tipo (param/retorno).
- **W291** ×4 — Espacios al final de línea: elimínalos.
- **ANN201** ×3 — Añade anotaciones de tipo (param/retorno).
- **D103** ×3 — Docstring para funciones a nivel de módulo.
- **S311** ×2 — Posible riesgo de seguridad (Bandit).
- **W293** ×2 — Revisa estilo/seguridad relacionado con la regla.
- **D100** ×1 — Añade docstring al módulo (propósito general).
- **I001** ×1 — Ordena imports (isort).

## Tipado estático (mypy)
```text
Success: no issues found in 1 source file

```
## Seguridad (Bandit)
```text
Run started:2025-10-14 18:45:55.371976

Test results:
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_calls.html#b311-random
   Location: /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:94:22
93	            # IA roll for a random hand.
94	            ia_hand = random.randint(0, 2)
95	

--------------------------------------------------
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.7.9/blacklists/blacklist_calls.html#b311-random
   Location: /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py:121:22
120	            choice_list.append("Shotgun")
121	            ia_hand = random.randint(0, 3)
122	

--------------------------------------------------

Code scanned:
	Total lines of code: 132
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
/home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_04/RockPaperScissors.py - A (52.95)

```