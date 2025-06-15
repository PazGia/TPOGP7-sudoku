import time
from sudoku_generator import SudokuGenerator
from sudoku_backtracking import BacktrackingSolver
from sudoku_branch_bound import BranchBoundSolver

def correr_experimento(dificultad, repeticiones):
    generador = SudokuGenerator()
    resultados = {
        "Backtracking": {"tiempos": [], "nodos": []},
        "Branch&Bound": {"tiempos": [], "nodos": []}
    }

    for _ in range(repeticiones):
        tablero = generador.generar_sudoku(dificultad)

        # Backtracking
        solver_bt = BacktrackingSolver(tablero)
        inicio = time.time()
        solver_bt.resolver()
        fin = time.time()
        resultados["Backtracking"]["tiempos"].append(fin - inicio)
        resultados["Backtracking"]["nodos"].append(solver_bt.nodos_explorados)

        # Branch & Bound
        solver_bb = BranchBoundSolver(tablero)
        inicio = time.time()
        solver_bb.resolver()
        fin = time.time()
        resultados["Branch&Bound"]["tiempos"].append(fin - inicio)
        resultados["Branch&Bound"]["nodos"].append(solver_bb.nodos_explorados)

    return resultados

def imprimir_resultados(resultados):
    for algoritmo in resultados:
        tiempos = resultados[algoritmo]["tiempos"]
        nodos = resultados[algoritmo]["nodos"]

        tiempo_promedio = sum(tiempos) / len(tiempos)
        nodos_promedio = sum(nodos) / len(nodos)

        print(f"{algoritmo}:")
        print(f"  Tiempo promedio: {tiempo_promedio:.4f} segundos")
        print(f"  Nodos promedio: {nodos_promedio:.0f}")
        print()

if __name__ == "__main__":
    dificultad = "facil"  # podes cambiarlo a facil, medio o dificil
    repeticiones = 10

    resultados = correr_experimento(dificultad, repeticiones)
    imprimir_resultados(resultados)
