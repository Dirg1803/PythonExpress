lista = ['a','b','c','d']

for letra in lista:
    numero_letra = lista.index(letra)+1
    print(f"Letra {numero_letra}: {letra}")


lista1 =['pablo','laura','fede','luis','julia']

for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("nombre que no comienza con l: " +nombre )


        numeros=[1,2,3,4,5]
        mi_valor=0

for numero in numeros:
    mi_valor=mi_valor+numero

    print(mi_valor)