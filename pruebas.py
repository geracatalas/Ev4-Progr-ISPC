import unittest
from clases import Arco

class TestArco(unittest.TestCase):
    def test_tirar(self):
        arco = Arco(50, 45)  # Fuerza de tiro: 50N, ángulo: 45 grados
        distancia = arco.tirar()
        self.assertAlmostEqual(distancia, 254.84, delta=1)  # Delta indica cuanto es lo maximo que puede variar entre el resultado esperado y el resultado obtenido

    def test_ajustar(self):
        arco = Arco(50, 45)
        arco.ajustar(60, 30)  # Ajusta la fuerza a 60N y el ángulo a 30 grados
        self.assertEqual(arco.fuerza_tiro, 60)
        self.assertEqual(arco.angulo, 30)

    def test_calcular_puntaje(self):
        arco = Arco(50, 45)
        puntaje = arco.calcular_puntaje(250)  # Objetivo a 250 metros
        self.assertEqual(puntaje, 10)

    def test_str(self):
        arco = Arco(50, 45)
        self.assertEqual(str(arco), "Arco con fuerza de 50N y ángulo de 45 grados")

if __name__ == "__main__":
    unittest.main()
