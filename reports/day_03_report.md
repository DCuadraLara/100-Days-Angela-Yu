# day_03 — Code Review (Nivel Día 3)

## Resumen ejecutivo
- **Correctness:** revisar entradas/salidas y casos borde.
- **Estilo/PEP8:** ver sección de *Estilo (Ruff/Black/Isort)*.
- **Robustez:** maneja errores explícitos cuando haya `input()` o archivos.
- **Legibilidad:** nombres claros, funciones pequeñas, comentarios puntuales.

## Hallazgos
### Estilo (Ruff)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:50:101 E501 Line too long (110 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:51:101 E501 Line too long (108 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:53:101 E501 Line too long (108 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:55:101 E501 Line too long (104 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:60:101 E501 Line too long (107 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:82:5 ANN201 Missing return type annotation for public function `reset_player`
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:111:33 W291 Trailing whitespace
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:114:101 E501 Line too long (103 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:116:27 W291 Trailing whitespace
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:117:101 E501 Line too long (101 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:127:1 W293 Blank line contains whitespace
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:128:33 W291 Trailing whitespace
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:129:101 E501 Line too long (118 > 100)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:131:101 E501 Line too long (135 > 100)
_Referencia_: https://peps.python.org/pep-0008/

### Complejidad (Radon)
- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py:82 CC=1 (function) reset_player

## Correcciones sugeridas (diffs no destructivos)
```diff
# Ruff
--- exercises/day_03/infinite_tower_maze.py
+++ exercises/day_03/infinite_tower_maze.py
@@ -108,12 +108,12 @@
 
         player_choice = input("\nChoose wisely: \nA \nB\n\n").upper().strip()
 
-        if player_choice == "A": 
+        if player_choice == "A":
             print(f"You burned yourself with super duper candle!\n {quests['death']['text']}")
         else:
             print(f"You manage to avoid some traps, oh that's... a door?\n {quests['escape']['text']}")
 
-elif player_choice == "B": 
+elif player_choice == "B":
     print(f"At midnight you hear a strange noise, its a monster coming!\n {quests['death']['text']}")
 else:
     print(f"\n{quests['quest03']['text']}\n") # Quest 03 -- Windows.
@@ -124,8 +124,8 @@
             print(f"{key} {value}")
 
         player_choice = input("\nChoose wisely: \nA \nB\n\n").upper().strip()
-        
-        if player_choice == "A": 
+
+        if player_choice == "A":
             print(f"You slice with that floor and broke your head, holy that's not lucky\n {quests['death']['text']}")
         else:
             print(f"The rune started to do so much noise, you see many lights! What¿? You are on home...\n {quests['escape']['text']}")

Would fix 4 errors (1 additional fix available with `--unsafe-fixes`).

# Black
--- /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py	2025-10-14 18:22:56.290874+00:00
+++ /home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py	2025-10-14 18:23:07.664603+00:00
@@ -1,13 +1,13 @@
-
 """We gonna create a Infinite Tower Maze.
 
 The player will have several choices to go on a way A, B or C.
 You must pick only one.
 """
 
-print(r'''
+print(
+    r'''
 
                          |\
                          |_\
                          |
                          |
@@ -32,53 +32,53 @@
      _/     ###  #########8###888888\ '    #  ####
     /     /    #####  \     'chelle  \_'    #   ####
    |                   |    |  _   98  \       _/  \
                         \_   \/         \__   /     \
 
-''')
+'''
+)
 
 print("\n*** Welcome to the Infinite Tower Maze ***\n")
-print("Your mission is to get out of this infinite loop, but please dont die on the process haha\n "
-      "¿Would you be able to do it? or you just gonna get lost on the way home...\n")
+print(
+    "Your mission is to get out of this infinite loop, but please dont die on the process haha\n "
+    "¿Would you be able to do it? or you just gonna get lost on the way home...\n"
+)
 
 # Random input to start it and have some gameplay.
 input("Breath one more time and feel the magic before you start your adventure...\n\n\n")
 
 
 # Quest list.
 quests = {
-    "quest01":{
+    "quest01": {
         "text": "You wake up on a strange room, that's not your house... wait you see some dumb decoration.\n"
-                "You see a mechanism on the wall near the door, you want to see what's outside the room...",
+        "You see a mechanism on the wall near the door, you want to see what's outside the room...",
         "options": {
             "A": "Press that mechanism.. oh wait the door its still closed. Suddenly the wall start moving."
-                 "There is a hole now with some stairs!",
+            "There is a hole now with some stairs!",
             "B": "You prefer to ignore it and just try to sleep again, maybe you wake up on your room.",
-            "C": "You decided to see if there is other way... oh well the room have some windows."
-        }
+            "C": "You decided to see if there is other way... oh well the room have some windows.",
+        },
     },
-    "quest02":{
+    "quest02": {
         "text": "You decided to go down stairs, but you need some light right? or... wanna go down darky.",
         "options": {
             "A": "Take a super candle, maybe that works? It have the super power of light hehe",
-            "B": "You go down darky, you trust your 'cat' eyes"
-        }
+            "B": "You go down darky, you trust your 'cat' eyes",
+        },
     },
-    "quest03":{
+    "quest03": {
         "text": "You went outside and see some runes on the air... You feel the power of them",
         "options": {
             "A": "Just ignore it and keep going on the roof",
-            "B": "Touch the runes? definitely a nice idea?"
-        }
+            "B": "Touch the runes? definitely a nice idea?",
+        },
     },
-    "death":{
-        "text": "You died Hero. Try again."
-    },
-    "escape":{
-        "text": "You escaped! Well done Hero."
-    },
+    "death": {"text": "You died Hero. Try again."},
+    "escape": {"text": "You escaped! Well done Hero."},
 }
+
 
 # Def reset function
 def reset_player():
     """Reset player input."""
     return ""
@@ -89,43 +89,51 @@
 
 
 # Quest 01 -- Room with mechanism.
 print(f"\n{quests['quest01']['text']}\n")
 
-while player_choice not in ["A", "B", "C"]: # A,B,C check.
+while player_choice not in ["A", "B", "C"]:  # A,B,C check.
     for key, value in quests["quest01"]["options"].items():
         print(f"{key} {value}")
 
     player_choice = input("\nChoose wisely: \nA \nB \nC\n\n").upper().strip()
 
 
 if player_choice == "A":
-    print(f"\n{quests['quest02']['text']}\n") # Quest 02 -- Stairs.
-    player_choice = reset_player() # Reset player choice so we can get into while.
+    print(f"\n{quests['quest02']['text']}\n")  # Quest 02 -- Stairs.
+    player_choice = reset_player()  # Reset player choice so we can get into while.
 
     while player_choice not in ["A", "B"]:  # A,B check.
         for key, value in quests["quest02"]["options"].items():
             print(f"{key} {value}")
 
         player_choice = input("\nChoose wisely: \nA \nB\n\n").upper().strip()
 
-        if player_choice == "A": 
+        if player_choice == "A":
             print(f"You burned yourself with super duper candle!\n {quests['death']['text']}")
         else:
-            print(f"You manage to avoid some traps, oh that's... a door?\n {quests['escape']['text']}")
+            print(
+                f"You manage to avoid some traps, oh that's... a door?\n {quests['escape']['text']}"
+            )
 
-elif player_choice == "B": 
-    print(f"At midnight you hear a strange noise, its a monster coming!\n {quests['death']['text']}")
+elif player_choice == "B":
+    print(
+        f"At midnight you hear a strange noise, its a monster coming!\n {quests['death']['text']}"
+    )
 else:
-    print(f"\n{quests['quest03']['text']}\n") # Quest 03 -- Windows.
+    print(f"\n{quests['quest03']['text']}\n")  # Quest 03 -- Windows.
     player_choice = reset_player()  # Reset player choice so we can get into while.
 
     while player_choice not in ["A", "B"]:  # A,B check.
         for key, value in quests["quest03"]["options"].items():
             print(f"{key} {value}")
 
         player_choice = input("\nChoose wisely: \nA \nB\n\n").upper().strip()
-        
-        if player_choice == "A": 
-            print(f"You slice with that floor and broke your head, holy that's not lucky\n {quests['death']['text']}")
+
+        if player_choice == "A":
+            print(
+                f"You slice with that floor and broke your head, holy that's not lucky\n {quests['death']['text']}"
+            )
         else:
-            print(f"The rune started to do so much noise, you see many lights! What¿? You are on home...\n {quests['escape']['text']}")
+            print(
+                f"The rune started to do so much noise, you see many lights! What¿? You are on home...\n {quests['escape']['text']}"
+            )

```
## Explicación de reglas detectadas
- **E501** ×9 — Línea demasiado larga: parte la expresión o extrae lógica.
- **W291** ×3 — Espacios al final de línea: elimínalos.
- **ANN201** ×1 — Añade anotaciones de tipo (param/retorno).
- **W293** ×1 — Revisa estilo/seguridad relacionado con la regla.

## Tipado estático (mypy)
```text
exercises/day_03/infinite_tower_maze.py:92: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:95: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:102: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:106: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:112: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:114: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:117: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:119: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:123: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:129: error: Value of type "object" is not indexable  [index]
exercises/day_03/infinite_tower_maze.py:131: error: Value of type "object" is not indexable  [index]
Found 11 errors in 1 file (checked 1 source file)

```
## Seguridad (Bandit)
```text
n/a
```
## Mantenibilidad (Radon MI)
```text
/home/runner/work/100-Days-Angela-Yu/100-Days-Angela-Yu/exercises/day_03/infinite_tower_maze.py - A (72.86)

```