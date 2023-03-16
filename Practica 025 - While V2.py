#Carlos Andres Riveramelo Del Toro
#20310382
#Practica 25 - Inteligencia Artificial

x=0
while x <= 30:
    
    if x == 4 or x == 6 or x == 10:
        print("Se saltó el valor", x, "de x.")
        x += 1
        continue
    if x ==15:
        print("Se rompió la ejecución del bucle cuando x valía ", x)
        break
    print("El valor de bucle es: ", x)
    x += 1
    