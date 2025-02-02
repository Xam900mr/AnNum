def metodo_montante(matriz, rest):
    n = len(rest)
    identidad = [[1 if i == j else 0 for j in range(n)]for i in range(n)]
    print(identidad)

    for k in range(n):
        print(k)
        actual = matriz[k][k] 
        print (actual)
        otras = [fila[k] for fila in matriz]
        print(otras)
        for j in range(n):
            if k != j:
                matriz[k][j] = 0
        print(matriz)

    pass

def main():

    matriz =([3, 6, -1],
    [7, -1, 2],
    [-2, -1, -1])

    valores = [25, 9, -6]

    metodo_montante(matriz, valores)

    
    """evaluador1 = False
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
    for i in range(n):
        for j in range(n):
            evaluador2 = False
            print(f"Ingrese el valor de X [{i+1}][{j+1}]:")
            while evaluador2 == False:
                try:
                    matriz [i][j] = float(input())
                    evaluador2 = True
                except ValueError:
                    print("ERROR: Debe ingresar un numero. Intente nuevamente:")
                    
        """
                

if __name__ == "__main__":
    main()

