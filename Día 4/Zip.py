from csv import list_dialects


nombre = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['lima','Madrid','Mexico']

combinados = list(zip(nombre,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")