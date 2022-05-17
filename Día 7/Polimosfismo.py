class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " la vaca dice muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " la vaca dice beee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

def animal_hablar(animal):
    animal.hablar()


animal_hablar(oveja1)