from pathlib import Path

base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada Familia.txt"))

print(guia.parent.parent)