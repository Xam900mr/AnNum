def main():
    
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
                    
        
                

if __name__ == "__main__":
    main()

def metodo_monatnte(matrix, accesoria):

    len(accesoria)
    pass