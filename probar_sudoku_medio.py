from sudoku_branch_bound import BranchBoundSolver  # cambiar si querés probar otro algoritmo
from sudoku_backtracking import BacktrackingSolver

import time

tablero_medio = [
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 7, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 2],
    [5, 1, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 1, 6, 8],
]
    
    
#solucionador = BranchBoundSolver(tablero_medio)
solucionador = BacktrackingSolver(tablero_medio)

inicio = time.time()
if solucionador.resolver():
    fin = time.time()

    print("Sudoku resuelto (medio):")
    for fila in solucionador.tablero:
        print(fila)

    print("Nodos explorados:", solucionador.nodos_explorados)
    print("Tiempo de ejecución:", fin - inicio, "segundos")
else:
    print("No tiene solución.")


#python3 probar_sudoku_medio.py