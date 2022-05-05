from random import randint


print("Adivina el numero")
nombre=input("Cuál es tu nombre: ")

print(f"Hola {nombre} ")
intentos=0
jugar=True

while jugar:
    while intentos < 3:
        numero = int(input("por favor elige un numero del 1 al 100 para adivinar: "))
        
        if numero <1 or numero > 100:
            print("El numero que inserto no está en el rango del 1 al 100")
        elif numero >= 1 and numero <=100:
            aleatorio=randint(1,101)
            if numero == aleatorio:
                print(f"El numero {numero} es el correcto ¡Felcidades!")
            elif numero > aleatorio:
                print(f"El numero {numero} es mayor al numero aleatorio ")
            else:
                print(f"El numero {numero} es menor al numero aleatorio ")
        intentos +=1
    intentar=input("Quieres volver a jugar? s/n: ")
    while True:
        if intentar == "n" or intentar == "N":
            jugar=False
            continue
        elif intentar == "s" or intentar == "S":
            jugar=True
            intentos=0
            continue
        else:
            print("Opción no valida")
    
    