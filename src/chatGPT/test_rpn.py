import unittest
from rpn import evaluar, RPNError


class TestRPN(unittest.TestCase):

    # ----------- OPERACIONES BASICAS -----------
    def test_suma(self):
        self.assertEqual(evaluar("3 4 +"), 7)

    def test_expresion_compleja(self):
        self.assertEqual(evaluar("5 1 2 + 4 * + 3 -"), 14)

    def test_multiplicacion(self):
        self.assertEqual(evaluar("2 3 4 * +"), 14)

    def test_division(self):
        self.assertEqual(evaluar("8 2 /"), 4)

    # ----------- NUMEROS Y SIGNOS -----------
    def test_negativo(self):
        self.assertEqual(evaluar("5 +/-"), -5)

    def test_float(self):
        self.assertEqual(evaluar("2.5 2 *"), 5)

    # ----------- FUNCIONES -----------
    def test_sqrt(self):
        self.assertEqual(evaluar("9 sqrt"), 3)

    def test_log(self):
        self.assertEqual(evaluar("100 log"), 2)

    def test_ln(self):
        self.assertAlmostEqual(evaluar("1 ln"), 0, places=5)

    def test_ex(self):
        self.assertAlmostEqual(evaluar("1 ex"), 2.71828, places=4)

    def test_10x(self):
        self.assertEqual(evaluar("2 10x"), 100)

    def test_inverso(self):
        self.assertEqual(evaluar("2 1/x"), 0.5)

    def test_potencia(self):
        self.assertEqual(evaluar("2 3 yx"), 8)

    # ----------- TRIGONOMETRIA -----------
    def test_sin(self):
        self.assertAlmostEqual(evaluar("90 sin"), 1, places=5)

    def test_cos(self):
        self.assertAlmostEqual(evaluar("0 cos"), 1, places=5)

    def test_tg(self):
        self.assertAlmostEqual(evaluar("45 tg"), 1, places=5)

    def test_asin(self):
        self.assertAlmostEqual(evaluar("1 asin"), 90, places=5)

    def test_acos(self):
        self.assertAlmostEqual(evaluar("1 acos"), 0, places=5)

    def test_atg(self):
        self.assertAlmostEqual(evaluar("1 atg"), 45, places=5)

    # ----------- PILA -----------
    def test_dup(self):
        self.assertEqual(evaluar("5 dup *"), 25)

    def test_swap(self):
        self.assertEqual(evaluar("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(evaluar("3 4 drop"), 3)

    # ----------- MEMORIA -----------
    def test_memoria(self):
        self.assertEqual(evaluar("10 1 STO 1 RCL"), 10)

    # ----------- ERRORES -----------
    def test_division_cero(self):
        with self.assertRaises(RPNError):
            evaluar("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluar("3 4 &")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluar("+")

    def test_resultado_invalido(self):
        with self.assertRaises(RPNError):
            evaluar("3 4")

    def test_swap_error(self):
        with self.assertRaises(RPNError):
            evaluar("5 swap")

    def test_drop_error(self):
        with self.assertRaises(RPNError):
            evaluar("drop")

    def test_funcion_sin_pila(self):
        with self.assertRaises(RPNError):
            evaluar("sqrt")

    def test_division_cero_inverso(self):
        with self.assertRaises(RPNError):
            evaluar("0 1/x")

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            evaluar("5 99 STO")

    def test_rcl_error(self):
        with self.assertRaises(RPNError):
            evaluar("RCL")


if __name__ == "__main__":
    unittest.main()