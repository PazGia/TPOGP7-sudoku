from sudoku_branch_bound import BranchBoundSolver  # cambiar si querés probar otro algoritmo
from sudoku_backtracking import BacktrackingSolver

import time

tablero_dificil = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [8, 4, 0, 0, 0, 0, 0, 0, 0]
]

solucionador = BranchBoundSolver(tablero_dificil)
#solucionador = BacktrackingSolver(tablero_dificil)



inicio = time.time()
if solucionador.resolver():
    fin = time.time()

    print("Sudoku resuelto (difícil):")
    for fila in solucionador.tablero:
        print(fila)

    print("Nodos explorados:", solucionador.nodos_explorados)
    print("Tiempo de ejecución:", fin - inicio, "segundos")
else:
    print("No tiene solución.")



#python3 probar_sudoku_dificil.py