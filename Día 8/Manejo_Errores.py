def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 1: "))
    print(n1+n2)
    print("Gracias por sumar" + n1)


try:
    #El codigo que queremos probar
    suma()
except TypeError:
    #El codigo a ejecutar si hay un error
    print("Estás intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    #codigo a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    #Se va a ejecutar codigo de todos modos osea siempre
    print("Eso fue todo y llegamos al finally")



def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()