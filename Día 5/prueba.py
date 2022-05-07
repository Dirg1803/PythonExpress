def suma_menores(suma):
    sum=0
    for n in suma:
        if n in range(0, 100):
            sum += n
    return sum


lista_numeros = [1, 2, 3, 4, 5,700,100,0,1]
print(suma_menores(lista_numeros))


def cantidad_pares(pares):
    cantidad = 0
    for n in pares:
        if n % 2 == 0:
            cantidad += 1
    return cantidad


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cantidad_pares(lista_numeros))