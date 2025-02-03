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

def main():
     
    matriz =([3, 6, -1],
    [7, -1, 2],
    [-2, -1, -1])

    valores = [25, 9, -6]
    
    evaluador1 = False
    print("Escriba el tamaño de la matriz:")
    while evaluador1 == False:
        try:
            n = int(input())
            if n > 0:
                evaluador1 = True
            else:
                print("ERROR: Debe de ser un numero positivo: Intente nuevamente:")
        except ValueError:
            print("ERROR: Debe ingresar un numero entero positivo. Intente nuevamente:")
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    valores = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n+1):
            evaluador2 = False
            if(j<n):
                print(f"Ingrese el valor de X [{i+1}][{j+1}]:")
                while evaluador2 == False:
                    try:
                        matriz [i][j] = float(input())
                        evaluador2 = True
                    except ValueError:
                        print("ERROR: Debe ingresar un numero. Intente nuevamente:")
            else:
                print(f"Ingrese el valor de la funcion {i+1}:")
                while evaluador2 == False:
                    try:
                        valores [i]= float(input())
                        evaluador2 = True
                    except ValueError:
                        print("ERROR: Debe ingresar un numero. Intente nuevamente:")

    resultado = metodo_montante(matriz, valores)

    print("El resultado es el siguiente")
    for i in range(3):
        print(f"X{i+1} = {resultado[i]}")        

if __name__ == "__main__":
    main()

