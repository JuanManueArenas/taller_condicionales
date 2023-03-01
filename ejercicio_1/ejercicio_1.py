# programa que lea las coordenadas cartesianas
print("------------------------------------------")
print("---NUMERO PARA INVERTIR:---")
print("------------------------------------------")
## input 
x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

#processing
if x == 0 and y == 0:
    print("El punto se encuentra en el origen.")
elif x == 0:
    print("El punto se encuentra sobre el eje y.")
elif y == 0:
    print("El punto se encuentra sobre el eje x.")
elif x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante.")
else:
    print("El punto se encuentra en el cuarto cuadrante.")