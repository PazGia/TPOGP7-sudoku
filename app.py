from flask import Flask, render_template, request, session
import copy
import time

from sudoku_generator import SudokuGenerator
from sudoku_branch_bound import BranchBoundSolver
from sudoku_backtracking import BacktrackingSolver

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # CAMBIAR en producción!

EMPTY_BOARD = [[0]*9 for _ in range(9)]

@app.route('/', methods=['GET', 'POST'])
def home():
    current_difficulty = request.form.get('difficulty', 'medio')
    initial_board = session.get('initial_board', EMPTY_BOARD)
    backtracking_solution = None
    branchbound_solution = None
    solution_data = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'generate':
            generator = SudokuGenerator()
            new_board = generator.generar_sudoku(current_difficulty)
            session['initial_board'] = new_board
            initial_board = new_board

        elif action == 'solve':
            # Resolver ambos métodos para mostrar ambos resultados
            board_to_solve = copy.deepcopy(initial_board)

            # Backtracking
            bt_solver = BacktrackingSolver(copy.deepcopy(board_to_solve))
            start_bt = time.time()
            solved_bt = bt_solver.resolver()
            end_bt = time.time()

            # Branch and Bound
            bnb_solver = BranchBoundSolver(copy.deepcopy(board_to_solve))
            start_bnb = time.time()
            solved_bnb = bnb_solver.resolver()
            end_bnb = time.time()

            if solved_bt and solved_bnb:
                backtracking_solution = bt_solver.tablero
                branchbound_solution = bnb_solver.tablero
                solution_data = {
                    'backtracking': {
                        'nodes_explored': bt_solver.nodos_explorados,
                        'time': end_bt - start_bt
                    },
                    'branchbound': {
                        'nodes_explored': bnb_solver.nodos_explorados,
                        'time': end_bnb - start_bnb
                    }
                }
            else:
                # Si falla alguno de los dos, mostramos tablero inicial y mensaje (podrías mejorar)
                backtracking_solution = None
                branchbound_solution = None
                solution_data = None

    return render_template(
        'index.html',
        difficulty=current_difficulty,
        initial_board=initial_board,
        backtracking_solution=backtracking_solution,
        branchbound_solution=branchbound_solution,
        solution_data=solution_data
    )

if __name__ == '__main__':
    app.run(debug=True)
