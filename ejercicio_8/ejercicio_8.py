#Programa que lea dos números enteros y averigüe si el uno es múltiplo del otro.

print("------------------------------------------")
print("---El resultado de las operaciones son:---")
print("------------------------------------------")


#input
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
#processing
if numero1 % numero2 == 0:
    print(numero1, "es múltiplo de", numero2)
elif numero2 % numero1 == 0:
    print(numero2, "es múltiplo de", numero1)
else:
    print("Los números no son múltiplos entre sí.")

