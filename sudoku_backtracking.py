class BacktrackingSolver:           # O(9^n) donde n es la cantidad de celdas vacías.
    # Recibo un tablero como parámetro
    # Creo atributos nodos explorados para contarlos
    def __init__(self, tablero):
        self.tablero = tablero
        self.nodos_explorados = 0

    # Creo un metodo que comprueba si vale poner un número en la celda      O(1) → verifica fila, columna y subcuadro en tamaño fijo (9x9)
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

    # Este metodo tiene el algoritmo de backtracking        O(9^n) → prueba los 9 números posibles en cada celda vacía
    def resolver(self):
        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0: #Si celda = 0
                    for numero in range(1, 10): #Pruebo del 1 al 9
                        self.nodos_explorados += 1 #+1 al contador de nodos explorados
                        if self.es_valido(fila, columna, numero):
                            self.tablero[fila][columna] = numero #Pongo el numero
                            if self.resolver(): #Llamada recursiva
                                return True
                            self.tablero[fila][columna] = 0  # backtracking: deshacemos porque este número no llevó a solución, probamos el siguiente
                    return False  # si ningún número funcionó, volvemos atrás
        return True  # si no quedan huecos, el Sudoku está resuelto

                            
                            
                            

