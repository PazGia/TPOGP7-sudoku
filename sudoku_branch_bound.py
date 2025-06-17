class BranchBoundSolver:     # Complejidad general: O(9^n) en el peor caso, donde n es la cantidad de celdas vacías.
    # Guardo el tablero inicial e inicio el contador de nodos
    def __init__(self, tablero):
        self.tablero = tablero
        self.nodos_explorados = 0

    # Metodo pa verificar validez del num que puse en la matriz.    O(1) (tamaño fijo 9x9)
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

    # Devuelvo una lista de números del 1 al 9 que se coloquen en una celda.    O(9)(máximo 9 candidatos posibles)
    def calcular_candidatos(self, fila, columna):  
        candidatos = []
        for numero in range(1, 10):
            if self.es_valido(fila, columna, numero):
                candidatos.append(numero)
        return candidatos


    def buscar_celda_mas_restringida(self):         #Complejidad O(81*9) constante, recorre el tablero completo
        min_candidatos = 10  # máximo posible es 9
        mejor_fila, mejor_columna = -1, -1

        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0: # Si celda vacia
                    candidatos = self.calcular_candidatos(fila, columna)
                    if len(candidatos) < min_candidatos:      #Aplica la heurística MRV (Minimum Remaining Values): busca la celda vacía con menor cantidad de candidatos válidos.
                        min_candidatos = len(candidatos)
                        mejor_fila, mejor_columna = fila, columna
                        if min_candidatos == 1: 
                            return mejor_fila, mejor_columna, candidatos

        if mejor_fila == -1:
            return None, None, []  # no hay más celdas vacías
        return mejor_fila, mejor_columna, self.calcular_candidatos(mejor_fila, mejor_columna)



    def calcular_cota_y_verificar(self):    # Complejidad O(81*9) revisa tablero completo y calcula cota
        suma_candidatos = 0  
        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0:
                    candidatos = self.calcular_candidatos(fila, columna)

                    # Si alguna celda vacía no tiene candidatos válidos, esta rama no es valida
                    if len(candidatos) == 0:
                        return None  # poda inmediata

                    suma_candidatos += len(candidatos) ** 2

        return suma_candidatos   # devolvemos la cota final para esta rama


  
    def resolver(self):     # Complejidad total: sigue siendo O(9^n) (búsqueda completa en el peor caso)

        fila, columna, candidatos = self.buscar_celda_mas_restringida()

        if fila is None:
            return True   # Sudoku resuelto (no quedan celdas vacías)

        if len(candidatos) == 0:
            return False   # Poda directa: rama inviable

        for numero in candidatos:
            self.tablero[fila][columna] = numero
            self.nodos_explorados += 1

            cota_actual = self.calcular_cota_y_verificar()

            if cota_actual is not None:   # Solo continúa si no hay inviabilidad
                if self.resolver():
                    return True

            self.tablero[fila][columna] = 0   # backtracking

        return False