mi_archivo = open('prueba.txt')

print(mi_archivo.readline())

print(mi_archivo.readline().rstrip().upper())

print(mi_archivo.readline())
mi_archivo.close()
