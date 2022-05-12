from pathlib import Path

carpeta = Path('C:/Users/066453781/Desktop/otro_archivo') / 'otro_archivo.txt'

mi_archivo = open(carpeta)
print(mi_archivo.read())