# Sudoku Solver con Backtracking y Branch & Bound
Este proyecto se conforma de una aplicación que permite visualizar y comparar la resolución de sudokus mediante dos algoritmos: Backtracking y Branch & Bound.

# Requisitos previos
Antes de ejecutar el proyecto, hay que asegurarse de tener lo siguiente instalado:
Python 3.0 o superior
Visual Studio Code (recomendado)
Extensión Python Debugger for VS Code (Microsoft)
Flask

Para instalar Flask, se puede ejecutar: pip install flask

# La aplicación
La aplicación se divide en dos partes principales:

1.  Interfaz Web
Cómo ejecutarla:
    Abrí una terminal en la carpeta del proyecto.
    Ejecutá el servidor con: python3 app.py
    Abrí tu navegador e ingresá a:  http://127.0.0.1:5000
La aplicación cuenta con una interfaz visual sencilla que permite generar sudokus aleatorios en tres niveles de dificultad: fácil, medio y difícil. Brinda la posibilidad de resolverlos utilizando dos enfoques algorítmicos diferentes: Backtracking y Branch & Bound. Una vez resuelto el tablero, se muestran las tres versiones (el sudoku generado y ambas soluciones), junto con una tabla comparativa que detalla la cantidad de nodos explorados y el tiempo de ejecución de cada algoritmo, complementado con gráficos estadísticos para facilitar el análisis.

2.  Archivos de prueba
Se puede ejecutar cada tipo de dificultad directamente desde archivos de prueba individuales:
probar_sudoku_facil.py
probar_sudoku_medio.py
probar_sudoku_dificil.py


Se puede probar de la siguiente manera:
    Abrí el archivo deseado en VS Code.
    Se puede usar Run Python File (ícono ▶ ️ arriba a la derecha) para iniciar la prueba
    
    Tip: Elegí el algoritmo
    Dentro de los archivos, podés elegir qué algoritmo ejecutar comentando/descomentando:
    solucionador = BranchBoundSolver(tablero_facil)
    #solucionador = BacktrackingSolver(tablero_facil)

3.  Archivo extra: probar.py
Se prueba con Run Python File (ícono ▶ ️ arriba a la derecha).
Este script reproduce el mismo flujo que la interfaz web: genera un Sudoku aleatorio, lo resuelve utilizando ambos algoritmos (Backtracking y Branch & Bound) y muestra en consola el tiempo de ejecución y la cantidad de nodos explorados . Es ideal para realizar pruebas rápidas sin necesidad de abrir el navegador.

