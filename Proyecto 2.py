def Biergevieta(coeficientes,grado):
    a = coeficientes # Se copian los coeficientes del polinomio
    X = [0] * grado  # Se crea una lista para almacenar las raíces (inicialmente llena de ceros)
    for j in range(grado): #Iteracion para encontrar raices
        X[j] = - a[-1] / a[-2]  # Primera aproximación de la raíz
        while True:  #Se repite hasta encontrar la raiz
            P = [0] * len(a)
            Pprim = [0] * (len(a)-1)
            for i in range(len(a)):  #Calcula cada P y P-prima
                if(i>0):
                    P[i] = P[i-1] * X[j] + a[i]
                else:
                    P[i] = a[i]
                if (i != len(a)-1):
                    if(i>0): 
                        Pprim[i] = Pprim[i-1] * X[j] + P[i]
                    else:
                        Pprim[i] = P[i]
            if (P[-1] != 0): #Detecta si encontro la raiz
                X[j] = X[j] - (P[-1] / Pprim[-1])
            else:
                break
        a = P[:-1]
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