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
        result = Simulations.classicDinamicSystem(state,graph,1)
        s = [
            [0],
            [0],
            [12],
            [5],
            [1],
            [9]
        ]
        for i in range(len(result)):
            self.assertEqual(result[i][0],s[i][0]);

    # Rendijas clasico con probabilidaades
    def test_rendijasProbabilistico(self):
        r= Simulations.nSlit(2,5,3)
        res=[0.0, 0.0, 0.0, 0.1665, 0.1665, 0.333, 0.1665, 0.1665]
        self.assertEqual(r,res)

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
