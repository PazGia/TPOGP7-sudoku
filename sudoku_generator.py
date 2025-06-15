import random
import copy

class SudokuGenerator:
    def __init__(self):
        self.tablero = [[0 for _ in range(9)] for _ in range(9)]
    
    def es_valido(self, fila, columna, numero):
        if numero in self.tablero[fila]:
            return False
        if numero in [self.tablero[i][columna] for i in range(9)]:
            return False
        
        inicio_fila = (fila // 3) * 3
        inicio_columna = (columna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.tablero[inicio_fila + i][inicio_columna + j] == numero:
                    return False
        return True

    def resolver_aleatorio(self):
        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0:
                    numeros = list(range(1, 10))
                    random.shuffle(numeros)
                    for numero in numeros:
                        if self.es_valido(fila, columna, numero):
                            self.tablero[fila][columna] = numero
                            if self.resolver_aleatorio():
                                return True
                            self.tablero[fila][columna] = 0
                    return False
        return True

    def generar_tablero_resuelto(self):
        self.resolver_aleatorio()
        return copy.deepcopy(self.tablero)

    def quitar_numeros(self, tablero_resuelto, cantidad_a_dejar):
        tablero = copy.deepcopy(tablero_resuelto)
        posiciones = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(posiciones)
        cantidad_a_borrar = 81 - cantidad_a_dejar

        for i in range(cantidad_a_borrar):
            fila, columna = posiciones[i]
            tablero[fila][columna] = 0

        return tablero

    def generar_sudoku(self, dificultad):
        if dificultad == "facil":
            cantidad_a_dejar = 45
        elif dificultad == "medio":
            cantidad_a_dejar = 30
        elif dificultad == "dificil":
            cantidad_a_dejar = 15
        else:
            raise ValueError("Dificultad no válida")

        solucion = self.generar_tablero_resuelto()
        tablero_incompleto = self.quitar_numeros(solucion, cantidad_a_dejar)
        return tablero_incompleto
