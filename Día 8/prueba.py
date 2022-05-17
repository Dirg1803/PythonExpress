import unittest
import camia_texto


class ProobarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen día"
        resultado = camia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()