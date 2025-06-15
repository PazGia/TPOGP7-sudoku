from sudoku_branch_bound import BranchBoundSolver  # cambiar si querés probar otro algoritmo
from sudoku_backtracking import BacktrackingSolver

import time

tablero_medio = [
    [0, 3, 9, 0, 0, 2, 0, 0, 0],
    [0, 6, 7, 3, 0, 0, 0, 2, 8],
    [8, 2, 4, 0, 6, 7, 0, 9, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 0, 0, 0, 0, 5, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   
    [6, 4, 0, 0, 2, 5, 8, 0, 7],
    [2, 0, 0, 7, 1, 0, 3, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
]
    
    
solucionador = BranchBoundSolver(tablero_medio)
#solucionador = BacktrackingSolver(tablero_medio)

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