def inter_lagrange(tabla, x):
    #Decalaramos una variable donde al amcenaremos la Y estimada por el proceso de interpolacion
    Y_estimada = 0
    #Declarsmos el numerador y el denominador de la division que se realizara
    numerador = 1
    denominador = 1
    # Iniciamos con el proceso para obtener el numerador y denominador de cada fraccion que se va a a sumar
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i != j:
                numerador = numerador * (x -tabla[j][0])
        numerador = numerador * tabla[i][1]

        for j in range(len(tabla)):
            if i != j:
                denominador = denominador * (tabla[i][0] -tabla[j][0])
        #Sumamos la fraccion a la Y_estimada
        Y_estimada += (numerador/denominador)
        #Reiniciamos el numerador y el numerador para la proxima iteracion
        numerador = 1
        denominador = 1
    #Retornamos el valor estimado de Y para X
    return Y_estimada

def lectura_datos():
    Datos = []
    i=0
    while True:
        while True:
            try:
                x = float(input(f"Ingrese el valor de x{i+1} = "))
                if any(x == dato[0] for dato in Datos):  # Verifica si x ya existe en Datos
                    print("ERROR: El valor de x ya fue ingresado. Ingrese un valor diferente.")
                    continue
                break
            except ValueError:
                print("ERROR: ingrese un valor numerico")

        while True:
            try:
                y = float(input(f"Ingrese el valor de y{i+1} = "))
                break
            except ValueError:
                print("ERROR: ingrese un valor numerico")
        
        Datos.append([x, y])
        i += 1

        if i >= 2:
            print('¿Desea ingresar otro conjunto de puntos?')
            opcion = input("Si / No\n")
            if opcion == 'si' or opcion == 'Si' or opcion == 'SI' or opcion == 'sI':
                continue
            else:
                break
    
    while True:
        try:
            X_estimar = float(input("Ingrese el valor de x para el cual se quiere interpolar el valor de y\n x = "))
            if any(X_estimar == dato[0] for dato in Datos):  # Verifica si x ya existe en Datos
                print("ERROR: El valor de x ya fue ingresado. Ingrese un valor diferente.")
                continue
            break
        except ValueError:
            print("ERROR: ingrese un valor numerico")
    
    
    return Datos, X_estimar

def main():
    while True:
        Tabla_Valores, X_estimar = lectura_datos()
        Y_estimada = inter_lagrange(Tabla_Valores, X_estimar)
        print(f'El valor estimado de Y({X_estimar}) es de : {Y_estimada}')

        print('¿Desea ingresar otros datos para interpolar?\n')
        opcion = input("Si / No\n")
        if opcion == 'si' or opcion == 'Si' or opcion == 'SI' or opcion == 'sI':
            continue
        else:
            break
if __name__ == "__main__":
    main()
