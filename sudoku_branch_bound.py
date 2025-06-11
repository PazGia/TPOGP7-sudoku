class SudokuSolver:
    def __init__(self, tablero):
        self.tablero = tablero
        self.nodos_explorados = 0

    def es_valido(self, fila, columna, numero):
        # Verificar fila
        if numero in self.tablero[fila]:
            return False

        # Verificar columna
        for i in range(9):
            if self.tablero[i][columna] == numero:
                return False

        # Verificar subcuadro 3x3
        inicio_fila = (fila // 3) * 3
        inicio_columna = (columna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.tablero[inicio_fila + i][inicio_columna + j] == numero:
                    return False

        return True

    def buscar_celda_con_menos_opciones(self):
        min_opciones = 10 #Inicializamos con el peor caso: 10 opciones (más que cualquier cantidad posible)
        mejor_celda = None

        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0:  # Solo analizamos las celdas vacías (celdas con 0)
                    opciones = 0
                    for numero in range(1, 10): # Probamos todos los números del 1 al 9 en la celda actual
                        if self.es_valido(fila, columna, numero):   # Si el número es válido para esa posición, sumamos una opción
                            opciones += 1 #es la cota!  la cantidad de opciones válidas que tiene cada celda vacía.

                    if opciones < min_opciones: # Si esta celda tiene menos opciones que la mejor que teníamos, la guardamos
                        min_opciones = opciones
                        mejor_celda = (fila, columna)

                    if min_opciones == 1:   # Si encontramos una celda con solo 1 opción, es la más restringida posible, salimos directamente
                        return mejor_celda

        return mejor_celda # Devolvemos la celda vacía con la menor cantidad de opciones posibles

    def resolver(self):
        celda = self.buscar_celda_con_menos_opciones()
        if not celda:
            return True  # No quedan celdas vacías, el Sudoku está resuelto

        fila, columna = celda

        for numero in range(1, 10):
            self.nodos_explorados += 1
            if self.es_valido(fila, columna, numero):
                self.tablero[fila][columna] = numero
                if self.resolver():
                    return True
                self.tablero[fila][columna] = 0  # backtracking: deshacemos porque este número no llevó a solución

        return False
