import unittest
from .service import calcular_emisiones_carbono

# Create your tests here.
class TestCalculoEmisiones( unittest.TestCase):
    def test_calcular_emisiones_carbono_defecto(self):
        # Caso de prueba 1: Consumo positivo
        resultado_obtenido = calcular_emisiones_carbono(100)
        self.assertEqual(resultado_obtenido, 40.0)

    def test_calcular_emisiones_carbono_error(self):
        # Caso de prueba 2: Consumo negativo
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)

    def test_calcular_emisiones_carbono_factor_personalizado(self):
        # Caso de prueba 3: Factor de emisión personalizado
        resultado_obtenido = calcular_emisiones_carbono(200, factor_emision=0.5)
        self.assertEqual(resultado_obtenido, 100.0)


