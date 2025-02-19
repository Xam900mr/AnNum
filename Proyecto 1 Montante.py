def metodo_montante(matriz, rest):
    #Obtenemos el tamano de la matriz
    n = len(rest)

    #Generamos una matriz identidad de tamano n
    identidad = [[1 if i == j else 0 for j in range(n)]for i in range(n)]

    #Declaramos el primer pivote
    pivote_ant = 1

    #Creamos una iteracion para resolver la matriz
    for k in range(n):

        #Guardamos el valor de la posicion (k,k) que sera con el que estemos trabajando (pivote actual)
        actual = matriz[k][k] 

        #Guardamos la columna k con la cual tambien estaremos trabajando
        otras = [fila[k] for fila in matriz]

        #Creamos otra iteracion en la cual haremos que todas las pocisiones en la columna k a excepcion de (k,k) sean 0
        for j in range(n):
            if k != j:
                matriz[j][k] = 0

        #Creamos otra iteracion donde los valores por arriba de (k,k) en la digonal sean igual a este
        for i in range(k):
            matriz[i][i] = actual

        # Modificamos los valores de la matriz usando el método de Montante
        for i in range(n):
            if i != k:
                for j in range(k+1, n):
                    matriz[i][j] = (actual * matriz[i][j] - otras[i] * matriz[k][j]) // pivote_ant 

        #Realizamos el mismo procedimiento pero con la matriz identidad
        for i in range(n):
            if i != k:
                for j in range(n):
                    identidad[i][j] = (actual * identidad[i][j] - otras[i] * identidad[k][j]) // pivote_ant
        #Modificamos el pivote anterior
        pivote_ant = actual

    #Una vez obtenida la determinanate y la Adjunta obtenemos la inversa
    Determinante = pivote_ant
    Adjunta = identidad
    inverversa = Adjunta
    for i in range(n):
        for j in range(n):
            inverversa[i][j] = inverversa[i][j] / Determinante 
    
    Valores_resultantes = [0] * n

    for i in range(n):
        for j in range(n):
            Valores_resultantes[i] = Valores_resultantes[i] + rest[j] * inverversa[i][j]
        Valores_resultantes[i] = round(Valores_resultantes[i])

    return Valores_resultantes

def pivoteo(matriz, actual, siguiente):

    #Realizamos el cambio de filas en la matriz
    matriz[actual], matriz[siguiente] = matriz[siguiente], matriz[actual]

    return matriz

def validar (matriz):
    n = len(matriz)
    for i in range(n):
            if matriz[i][i] == 0:
                return True
    return False

def solucionar_matriz(matriz, rest):
    n = len(rest)
    
    #Validamos que la matriz no algun 0 en la diagonal
    cero = validar(matriz)

    #Si llegara a tener un 0 en la diagonal realizamos movimientos en las filas 

    actual = 0 #Iniciamos el contador de la casilla que vamos a cambiar
    siguiente = actual + 1 #Iniciamos el contador de la casilla con la cual la vamos a cambiar
    iteraciones = 0 #iniciamos el contador de iteraciones para realizar los cambios

    while cero and iteraciones < n:

        #Llamamos a la funcion pivoteo que realizara los cambios en la matriz
        matriz = pivoteo(matriz, actual, siguiente)

        #Volvemos a validar matriz
        cero = validar(matriz)

        #Si hay 0 avanzamos en la matriz para realizar cambios
        if cero:

            #Si siguiente no ha llegado al ultima fila de la matriz avanzamos
            if siguiente + 1 < n:
                actual = actual +1
                siguiente = actual +1

            #Si no volvemos a cambiar desde la primer fila e incrementamos las iteraciones
            else:
                actual = 0
                siguiente = actual +1
                iteraciones += 1
        #Salimos de la funcion

    #Validamos que si podemos realizar el metodo motante
    if cero:
         print("ERROR: la matriz ingresada no es apta para el metodo montante, ya que no hay una combinacion de filas con una diagonal que no tenga 0, intente nuevamente con otra matriz")
         return False
    else:
        #Se calcula el resultado por el metodo montante
        resultado = metodo_montante(matriz, rest)
        return resultado

def main():
     op = 1
     while op == 1:
        evaluador1 = False
        #Se ingresa el tamaño de la matriz
        print("Escriba el tamaño de la matriz:")
        #Se comprueba que el valor sea un numero entero positivo
        while evaluador1 == False:
            try:
                n = int(input())
                if n > 0:
                    evaluador1 = True
                else:
                    print("ERROR: Debe de ser un numero positivo: Intente nuevamente:")
            except ValueError:
                print("ERROR: Debe ingresar un numero entero positivo. Intente nuevamente:")
        #Se crea la Matriz junto a los valores de sus funciones
        matriz = [[0 for _ in range(n)] for _ in range(n)]
        valores = [0 for _ in range(n)]

        #Se evalua que la matriz sea invertible
        while True:
            for i in range(n):
                for j in range(n+1):
                    evaluador2 = False
                    if(j<n):
                        print(f"Ingrese el valor de X [{i+1}][{j+1}]:")
                        #se comprueba que los valores dentro de la matriz sean numeros
                        while evaluador2 == False:
                            try:
                                matriz [i][j] = float(input())
                                evaluador2 = True
                            except ValueError:
                                print("ERROR: Debe ingresar un numero. Intente nuevamente:")
                    else:
                        print(f"Ingrese el valor de la funcion {i+1}:")
                        #se evalua que los valores de los resultados sean numeros
                        while evaluador2 == False:
                            try:
                                valores [i] = float(input())
                                evaluador2 = True
                            except ValueError:
                                print("ERROR: Debe ingresar un numero. Intente nuevamente:")
            try:
                resultado = solucionar_matriz(matriz, valores)
                break
            except ZeroDivisionError:
                print("ERROR: la matriz ingresada no es invertible por ende no es apta para el metodo montante, intente nuevamente con otra matriz")

        if resultado:
            print("El resultado es el siguiente")
            for i in range(n):
                print(f"X{i+1} = {resultado[i]}")  


        opcion = input("Si / No\n")
        print('¿Desea calcular otra matriz?', opcion)
        if opcion == 'si' or opcion == 'Si' or opcion == 'SI' or opcion == 'sI':
            op = 1
        else:
            op = 0

        

if __name__ == "__main__":
    main()

