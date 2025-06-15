from sudoku_backtracking import BacktrackingSolver
from sudoku_generator import SudokuGenerator
from sudoku_branch_bound import BranchBoundSolver  # cambiar si querés probar otro algoritmo
import time


generador = SudokuGenerator()
tablero_dificil = generador.generar_sudoku("dificil")
tablero_dificil_backtracking= tablero_dificil

solucionador = BranchBoundSolver(tablero_dificil)

inicio = time.time()
if solucionador.resolver():
    fin = time.time()

    print("Sudoku resuelto (difícil):")
    for fila in solucionador.tablero:
        print(fila)

    print("B&B:")
    print("Nodos explorados:", solucionador.nodos_explorados)
    print("Tiempo de ejecución:", fin - inicio, "segundos")
else:
    print("No tiene solución.")



solucionadorbacktacking = BacktrackingSolver(tablero_dificil_backtracking)

inicio = time.time()
if solucionadorbacktacking.resolver():
    fin = time.time()

    print("Backtracking:")
   

    print("Nodos explorados:", solucionador.nodos_explorados)
    print("Tiempo de ejecución:", fin - inicio, "segundos")
else:
    print("No tiene solución.")