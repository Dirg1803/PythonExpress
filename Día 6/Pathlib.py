from pathlib import Path, PureWindowsPath

carpeta = Path('c:/Users/066453781/Documents/Cursos/Python/PythonExpress/Día 6/prueba.txt')

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)