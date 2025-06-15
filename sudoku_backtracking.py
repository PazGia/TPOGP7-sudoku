class BacktrackingSolver:
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




    def resolver(self):
        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0:
                    for numero in range(1, 10):
                        self.nodos_explorados += 1
                        if self.es_valido(fila, columna, numero):
                            self.tablero[fila][columna] = numero
                            if self.resolver():
                                return True
                            self.tablero[fila][columna] = 0  # backtracking: deshacemos porque este número no llevó a solución, probamos el siguiente
                    return False  # si ningún número funcionó, volvemos atrás
        return True  # si no quedan huecos, el Sudoku está resuelto

                            
                            
                            

