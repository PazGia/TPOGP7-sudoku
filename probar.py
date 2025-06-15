from sudoku_backtracking import BacktrackingSolver
from sudoku_generator import SudokuGenerator
from sudoku_branch_bound import BranchBoundSolver  # cambiar si querés probar otro algoritmo
import time
import copy

import copy

# Generás el tablero original
generador = SudokuGenerator()
tablero_dificil = generador.generar_sudoku("medio")

# Para Branch & Bound
tablero_para_bnb = copy.deepcopy(tablero_dificil)

# Para Backtracking
tablero_para_bt = copy.deepcopy(tablero_dificil)

print("Tablero generado vacio:")
for fila in tablero_dificil:
    print(fila)


solucionador_bnb = BranchBoundSolver(tablero_para_bnb)

inicio = time.time()
if solucionador_bnb.resolver():
    fin = time.time()

    print("Sudoku resuelto con Branch and Bound")
    for fila in solucionador_bnb.tablero:
        print(fila)

    print("B&B:")
    print("Nodos explorados:", solucionador_bnb.nodos_explorados)
    print("Tiempo de ejecución:", fin - inicio, "segundos")
else:
    print("No tiene solución.")

solucionador_bt = BacktrackingSolver(tablero_para_bt)
inicio = time.time()
if solucionador_bt.resolver():
    fin = time.time()

    print("Backtracking:")
    for fila in solucionador_bt.tablero:
        print(fila)

   

    print("Nodos explorados:", solucionador_bt.nodos_explorados)
    print("Tiempo de ejecución:", fin - inicio, "segundos")
else:
    print("No tiene solución.")