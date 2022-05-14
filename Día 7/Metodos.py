class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha voldado {metros} metros")

piolin = Pajaro('amarrillo','canario')
piolin.piar()