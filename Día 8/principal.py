import numeros

def preguntar():
    print("Bienvenido al Frmacia Python")

    while True:
        print("[P] - perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubo = input("Elija su Rubro: ").upper()
            ["P","F","C"].index(mi_rubo)
        except ValueError:
            print("ESa no es una opción validad")
        else:
            break

    numeros.decorador(mi_rubo)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción Validad")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()