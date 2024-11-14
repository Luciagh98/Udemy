import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):

#La función siempre tiene que empezar por TEST
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA") #Va a verificar si la función de todo
        #mayuscula cumple la condición que le esciribimos a mano BUEN DIA.

if __name__ == '__main__':
    unittest.main()

'----------------------------------------------------------------------'
'Ran 1 test in 0.000s)'
'OK'

#Sin embargo, si queremos que sea, por ejemplo, estilo titulo, nos dará error.
#Ya que upper pone todo en mayusculas, no solo las primeras.

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "Buen Dia")

if __name__ == '__main__':
    unittest.main()