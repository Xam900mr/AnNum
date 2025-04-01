def lectura_datos():
    Datos = []
    i=0
    while True:
        while True:
            try:
                x = float(input(f"Ingrese el valor de x{i+1}:"))
                if any(x == dato[0] for dato in Datos):  # Verifica si x ya existe en Datos
                    print("ERROR: El valor de x ya fue ingresado. Ingrese un valor diferente.")
                    continue
                break
            except ValueError:
                print("ERROR: ingrese un valor numerico")

        while True:
            try:
                y = float(input(f"Ingrese el valor de y{i+1}:"))
                break
            except ValueError:
                print("ERROR: ingrese un valor numerico")
        
        Datos.append([x, y])
        i += 1

        if i >= 2:
            print('¿Desea calcular otro polinomio?')
            opcion = input("Si / No\n")
            if opcion == 'si' or opcion == 'Si' or opcion == 'SI' or opcion == 'sI':
                continue
            else:
                break
    
    return Datos

def main():
    Tabla_Valores = lectura_datos()
if __name__ == "__main__":
    main()
