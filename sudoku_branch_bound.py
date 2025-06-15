class BranchBoundSolver:
    # Guardo el tablero inicial e inicio el contador de nodos
    def __init__(self, tablero):
        self.tablero = tablero
        self.nodos_explorados = 0

    # Metodo pa verificar validez del num que puse en la matriz
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

    # Devuelvo una lista de números del 1 al 9 que se coloquen en una celda.
    # Lo uso para conocer las posibles opciones antes de decidir.
    def calcular_candidatos(self, fila, columna):
        candidatos = []
        for numero in range(1, 10):
            if self.es_valido(fila, columna, numero):
                candidatos.append(numero)
        return candidatos

    # Uso heurística MRV - Minimum Remaining Values
    # Busco la celda con menores candidatos posibles
    # Si encuentra celda con 1 candidato PODO
    # Si no hay más celdas vacías devuelvo none - completo
    def buscar_celda_mas_restringida(self):
        min_candidatos = 10  # máximo posible es 9
        mejor_fila, mejor_columna = -1, -1

        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0: # Si celda vacia
                    candidatos = self.calcular_candidatos(fila, columna)
                    if len(candidatos) < min_candidatos:      #Aplica la heurística MRV (Minimum Remaining Values): busca la celda vacía con menor cantidad de candidatos válidos.
                        min_candidatos = len(candidatos)
                        mejor_fila, mejor_columna = fila, columna
                        if min_candidatos == 1:   # poda rápida si queda solo una opción
                            return mejor_fila, mejor_columna, candidatos

        if mejor_fila == -1:
            return None, None, []  # no hay más celdas vacías
        return mejor_fila, mejor_columna, self.calcular_candidatos(mejor_fila, mejor_columna)

    ## ------------------------------ COTA 1 ----------------
        # Calculo una cota heurísica para saber si vale la pena seguir explorando
        # Recorro las celdas vacías y sumo candidatos válidos
        # Si alguna tiene 0 devuelvo none
        # Si todas tienen al menos uno devuelve esa suma
        # Con esto puedo podar antes de hacer recursividad
    """   def calcular_cota_y_verificar(self):

            Calcula la cota total como la suma de candidatos válidos en todas las celdas vacías.
            Si alguna celda queda sin candidatos (cota local 0), retorna None para indicar que la rama es inviable.

            suma_candidatos = 0
            for fila in range(9):
                for columna in range(9):
                    if self.tablero[fila][columna] == 0:
                        candidatos = self.calcular_candidatos(fila, columna)
                        if len(candidatos) == 0:
                            return None   # poda inmediata por inviabilidad
                        suma_candidatos += len(candidatos)
            return suma_candidatos """

    ##---------------------------- COTA 2--------------------------

    def calcular_cota_y_verificar(self): # Added 'self' here
        """
        Calcula una cota para esta rama del árbol:
        - Para cada celda vacía, se calcula la cantidad de candidatos posibles.
        - Si alguna celda no tiene candidatos, se retorna None → se poda.
        - En lugar de sumar directamente los candidatos, se usa la suma de sus cuadrados.
          Esto penaliza más fuertemente las ramas con muchas posibilidades (menos prometedoras).

        Ejemplo:
        - Cota anterior (lineal): 3 candidatos + 3 + 2 = 8
        - Cota nueva (cuadrada): 9 + 9 + 4 = 22 → más alta = menos prometedora
        """
        suma_candidatos = 0  # inicializamos la cota total

        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0:
                    candidatos = self.calcular_candidatos(fila, columna)

                    # Si alguna celda vacía no tiene candidatos válidos, esta rama es inviable
                    if len(candidatos) == 0:
                        return None  # poda inmediata

                    # En lugar de sumar simplemente len(candidatos), usamos len(candidatos) ** 2
                    # Esto aumenta el "costo" de ramas con más incertidumbre
                    suma_candidatos += len(candidatos) ** 2

        return suma_candidatos   # devolvemos la cota final para esta rama


    # Llamo al metodo buscar celda mas restringida para elegir la mejor celda
    # Si no hay mas celdas devuelvo true osea resulto
    # Si la celda no tiene candidatos devuelvo false pues invalido
    # Si tengo candidatos pruebo cada uno, pongo el num en celda, contador +1,
    # Calculo la cota
        # Si es none PODO
        # Si NO es none aplico recursividad
    # Si no funciona con backtracking borro el numero
    # Si no funciona ninguno devuelve false
    def resolver(self):

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