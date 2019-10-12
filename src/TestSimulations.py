import unittest
import Complex as comp
import Simulations
import math


class TestSimulatons(unittest.TestCase):

    # Pruebas de la sección 3

    # Canicas clásico
    def test_canicasClasico(self):
        graph = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0]
        ]
        state = [
            [6],
            [2],
            [1],
            [5],
            [3],
            [10]
        ]
        result = Simulations.classicDinamicSystem(state, graph, 1)
        s = [
            [0],
            [0],
            [12],
            [5],
            [1],
            [9]
        ]
        for i in range(len(result)):
            self.assertEqual(result[i][0], s[i][0])

    # Rendijas clasico con probabilidaades
    # def test_rendijasProbabilistico(self):
    #     r = Simulations.nSlit(2, 5, 3)
    #     res = [0.0, 0.0, 0.0, 0.1665, 0.1665, 0.333, 0.1665, 0.1665]
    #     self.assertEqual(r, res)

    # Sistema cuántico de partícula en una línea

    def test_probabilidad(self):
        ket = [
            [comp.Complex(-3, -1)],
            [comp.Complex(0, -2)],
            [comp.Complex(0, 1)],
            [comp.Complex(2,0)]
        ]
        i = 2
        r = Simulations.probability(ket, i)
        s =  0.052624
        self.assertAlmostEqual(r,s)


    # Otras Pruebas

    def test_ProbAndTransition(self):
        pass

    def test_meanAndVariance(self):
        pass

    def test_ownValues(self):
        pass

    def test_Dynamic(self):
        pass


if __name__ == '__main__':
    unittest.main()
