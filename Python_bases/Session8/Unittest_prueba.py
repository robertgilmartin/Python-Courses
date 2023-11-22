# Queremos probar que la funcion retorna lo que esperamos en este caso tod0 en CAPS
import unittest
import Unittest


class ProbarCambiaTexto(unittest.TestCase):

    # Es OBLIGATORIO que la función empiece por 'test_' sino no funcionará
    def test_mayusculas(self):
        palabra = 'buen dia'
        result = Unittest.todo_mayuscula(palabra)
        self.assertEqual(result, 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()