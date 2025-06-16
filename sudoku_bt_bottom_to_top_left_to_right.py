class BacktrackingSolver:
    # Recibo un tablero como parámetro
    # Creo atributos nodos explorados para contarlos
    def __init__(self, tablero):
        self.tablero = tablero
        self.nodos_explorados = 0

    # Creo un método que comprueba si vale poner un número en la celda
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

    # Método de backtracking que recorre el tablero de abajo hacia arriba y derecha a izquierda
    def resolver(self):
        for fila in range(8, -1, -1):            # de fila 8 a 0 (abajo hacia arriba)
            for columna in range(8, -1, -1):     # de columna 8 a 0 (derecha a izquierda)
                if self.tablero[fila][columna] == 0:  # si celda vacía
                    for numero in range(1, 10):       # pruebo números del 1 al 9
                        self.nodos_explorados += 1    # aumento contador nodos explorados
                        if self.es_valido(fila, columna, numero):
                            self.tablero[fila][columna] = numero
                            if self.resolver():
                                return True
                            self.tablero[fila][columna] = 0  # deshago (backtracking)
                    return False
        return True  # sudoku resuelto (no quedan huecos)
