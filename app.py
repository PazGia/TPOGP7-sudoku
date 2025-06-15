from flask import Flask, render_template, request, session, redirect, url_for
import copy
import time

# Importa tus clases de los archivos
from sudoku_generator import SudokuGenerator
from sudoku_branch_bound import BranchBoundSolver
from sudoku_backtracking import BacktrackingSolver

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui' # ¡CAMBIA ESTO POR UNA CLAVE SEGURA EN PRODUCCIÓN!

# Tablero inicial vacío para la primera carga
EMPTY_BOARD = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

@app.route('/', methods=['GET', 'POST'])
def home():
    # Siempre obtenemos el tablero *inicial* de la sesión para operar sobre él
    # Esto asegura que ambos algoritmos resuelvan el mismo problema no resuelto.
    initial_board = session.get('initial_board', EMPTY_BOARD)
    
    # El tablero que se va a mostrar puede ser el inicial o la solución
    display_board = copy.deepcopy(initial_board) 
    
    solution_info = None
    error_message = None
    current_difficulty = request.form.get('difficulty', 'medio')

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'generate':
            generator = SudokuGenerator()
            new_board = generator.generar_sudoku(current_difficulty)
            session['initial_board'] = new_board # Guarda el NUEVO tablero inicial
            display_board = copy.deepcopy(new_board) # El tablero a mostrar es el nuevo tablero inicial
            solution_info = None 
            error_message = None

        elif action in ['solve_bnb', 'solve_bt']:
            # Usamos una copia del initial_board (el problema sin resolver)
            board_to_solve = copy.deepcopy(initial_board) 
            
            solver = None
            algorithm_name = ""

            if action == 'solve_bnb':
                solver = BranchBoundSolver(board_to_solve)
                algorithm_name = "Branch and Bound"
            elif action == 'solve_bt':
                solver = BacktrackingSolver(board_to_solve)
                algorithm_name = "Backtracking"
            
            if solver:
                start_time = time.time()
                if solver.resolver():
                    end_time = time.time()
                    display_board = solver.tablero # El tablero a mostrar es la solución
                    solution_info = {
                        "algorithm": algorithm_name,
                        "nodes_explored": solver.nodos_explorados,
                        "time": end_time - start_time
                    }
                    # No actualizamos 'initial_board' aquí, para que el próximo solver use el original.
                else:
                    error_message = f"El Sudoku no tiene solución para el algoritmo {algorithm_name}."
                    # Si no hay solución, 'display_board' ya contiene el initial_board original.
            else:
                error_message = "Error: Solucionador no especificado."

    # Pasar current_difficulty a la plantilla para mantener la selección
    return render_template('index.html', board=display_board, solution_info=solution_info, error_message=error_message, difficulty=current_difficulty)

if __name__ == '__main__':
    app.run(debug=True)