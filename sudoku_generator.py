import random
import copy

# Creo la clase para crear y resolver los tableros
# Inicializo tablero 9x9 lleno de 0
# Self.tablero es el atributo principal para la clase del generador
class SudokuGenerator:
    def __init__(self):
        self.tablero = [[0 for _ in range(9)] for _ in range(9)]

# Defino un metodo que verifica que puedo poner los numeros validos para sudoku (del 1 al 9)
# Divido fila y columna en 3 para identificar en q subcuadro estoy
# Y compruebo que el número no este en ningun slot
    def es_valido(self, fila, columna, numero):
        if numero in self.tablero[fila]: #verifica fila
            return False
        if numero in [self.tablero[i][columna] for i in range(9)]: #verifica columna
            return False
        
        inicio_fila = (fila // 3) * 3
        inicio_columna = (columna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.tablero[inicio_fila + i][inicio_columna + j] == numero: #verifica subcuadro
                    return False
        return True

# Defino un metodo para resolver el sudoku aleatorio con backtracking
    def resolver_aleatorio(self):
        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0: #si celda == 0
                    numeros = list(range(1, 10))
                    random.shuffle(numeros) #Intenta poner números del 1 al 9
                    #Si es valido lo agrega
                    for numero in numeros:
                        if self.es_valido(fila, columna, numero):
                            self.tablero[fila][columna] = numero
                            if self.resolver_aleatorio():
                                return True #Solucionado
                            self.tablero[fila][columna] = 0
                    return False #Si no puede colocar numero valido
        return True #Cuando tengo el tablero completo

# Defino un metodo que llama al método de resolver aleatorio para completar el sudoku
# Lo que hace es devolver el tablero resuelto para no modificarlo luego
    def generar_tablero_resuelto(self):
        self.resolver_aleatorio()
        return copy.deepcopy(self.tablero)
    
# Defino un metodo para que a partir de un tablero completo sacar números
# Cantidad a dejar es para definir cuantos numeros van a quedar (menos numeros es mas dificil)
# Se borran posiciones al azar    
    def quitar_numeros(self, tablero_resuelto, cantidad_a_dejar):
        tablero = copy.deepcopy(tablero_resuelto)
        posiciones = [(i, j) for i in range(9) for j in range(9)] #todas las posiciones del tablero
        random.shuffle(posiciones)
        cantidad_a_borrar = 81 - cantidad_a_dejar

        for i in range(cantidad_a_borrar):
            fila, columna = posiciones[i]
            tablero[fila][columna] = 0

        return tablero

# Defino un método para generar sudoku depende la dificultad
# Genero un tablero completo resuelto y borro números hasta que alcanzo la dificultad
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