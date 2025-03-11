def Biergevieta(coeficientes,grado):
    a = coeficientes
    X = [0] * grado
    X[0] = - a[grado] / a[grado-1]
    for j in range(grado):
        while True:
            P = [0] * len(a)
            Pprim = [0] * (len(a)-1)
            for i in range(grado):
                if(i>0):
                    P[i] = P[i-1] * X[j] + a[i]
                else:
                    P[i] = a[i]
                if (i != grado-1):
                    if(i>0): 
                        Pprim[i] = Pprim[i-1] * X[j] + P[i]
                    else:
                        Pprim[i] = P[i]
            if (P[len(P)-1] != 0):
                X[j] = X[j] - (P[len(P)-1] / Pprim[len(Pprim)-1])
            else:
                break
        a = [0] * (len(P)-1)
        for i in range(len(P)-1):
            a[i] = P[i]
    return X

def lectura_ecuacion():
    while True:
        try:
            grado = int(input("Ingrese el grado de la ecuación: "))
            if grado <= 0:
                print("El grado debe ser un número entero no negativo sin incluir el 0.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido.")

    coeficientes = []
    for i in range(grado+1):
        while True:
            try:
                coef = float(input(f"Ingrese el coeficiente de x^{grado-i}: "))
                coeficientes.append(coef)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    return coeficientes, grado

def main():
    coeficientes,grado = lectura_ecuacion()
    resultados = Biergevieta(coeficientes,grado)
    for i in range(len(resultados)):
        print(f"x{i+1} = {resultados[i]}")

if __name__ == "__main__":
    main()