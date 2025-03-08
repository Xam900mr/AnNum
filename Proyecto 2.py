def lectura_ecuacion():
    while True:
        try:
            grado = int(input("Ingrese el grado de la ecuación: "))
            if grado < 0:
                print("El grado debe ser un número entero no negativo.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    coeficientes = []
    for i in range(grado, -1, -1):
        while True:
            try:
                coef = float(input(f"Ingrese el coeficiente de x^{i}: "))
                coeficientes.append(coef)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    return coeficientes

def main():
    coeficientes = lectura_ecuacion()

if __name__ == "__main__":
    main()