import unittest
import Complex as comp
import Matrix
import math


class TestComplex(unittest.TestCase):
    def test_vector_add(self):
        v1 = [[comp.Complex(1, 1)], [comp.Complex(1, 2)], [
            comp.Complex(1, 3)], [comp.Complex(3, 5)]]
        v2 = [[comp.Complex(2, 8)], [comp.Complex(6, 2)], [
            comp.Complex(4, 4)], [comp.Complex(8, 0)]]
        s = [[comp.Complex(3, 9)], [comp.Complex(7, 4)], [
            comp.Complex(5, 7)], [comp.Complex(11, 5)]]
        p = Matrix.add(v1, v2)
        for i in range(len(p)):
            self.assertEqual(s[i][0].real, p[i][0].real)
            self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_vector_inverse(self):
        v1 = [[comp.Complex(1, 1)], [comp.Complex(1, 2)], [
            comp.Complex(1, 3)], [comp.Complex(3, 5)]]
        s = [[comp.Complex(-1, -1)], [comp.Complex(-1, -2)],
             [comp.Complex(-1, -3)], [comp.Complex(-3, -5)]]
        p = Matrix.inverse(v1)
        for i in range(len(p)):
            self.assertEqual(s[i][0].real, p[i][0].real)
            self.assertEqual(s[i][0].imag, p[i][0].imag)

        v1 = [[comp.Complex(6, -4)], [comp.Complex(7, 3)], [
            comp.Complex(4.2, -8.1)], [comp.Complex(0, -3)]]
        s = [[comp.Complex(-6, 4)], [comp.Complex(-7, -3)],
             [comp.Complex(-4.2, 8.1)], [comp.Complex(0, 3)]]
        p = Matrix.inverse(v1)
        for i in range(len(p)):
            self.assertEqual(s[i][0].real, p[i][0].real)
            self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_vector_scalarMultiplication(self):
        c = comp.Complex(8, 8)
        v1 = [[comp.Complex(1, 1)], [comp.Complex(1, 2)], [
            comp.Complex(1, 3)], [comp.Complex(3, 5)]]
        s = [[comp.Complex(-1, -1)], [comp.Complex(-1, -2)],
             [comp.Complex(-1, -3)], [comp.Complex(-3, -5)]]
        p = Matrix.inverse(v1)
        for i in range(len(p)):
            self.assertEqual(s[i][0].real, p[i][0].real)
            self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_add(self):
        v1 = [[comp.Complex(1, 1), comp.Complex(1, 1)], [
            comp.Complex(1, 2), comp.Complex(1, 1)]]
        v2 = [[comp.Complex(1, 1), comp.Complex(1, 1)], [
            comp.Complex(1, 2), comp.Complex(1, 1)]]
        s = [[comp.Complex(2, 2), comp.Complex(2, 2)], [
            comp.Complex(2, 4), comp.Complex(2, 2)]]
        p = Matrix.add(v1, v2)
        for i in range(len(p)):
            for j in range(len(p[0])):
                self.assertEqual(s[i][0].real, p[i][0].real)
                self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_inverse(self):
        v1 = [[comp.Complex(1, 1), comp.Complex(1, 1)], [
            comp.Complex(1, 2), comp.Complex(1, 1)]]

        s = [[comp.Complex(-1, -1), comp.Complex(-1, -1)], [
            comp.Complex(-1, -2), comp.Complex(-1, -1)]]
        p = Matrix.inverse(v1)
        for i in range(len(p)):
            for j in range(len(p[0])):
                self.assertEqual(s[i][0].real, p[i][0].real)
                self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_scalarMultiplication(self):
        c = comp.Complex(8, 8)
        v1 = [[comp.Complex(1, 1)], [comp.Complex(1, 2)], [
            comp.Complex(1, 3)], [comp.Complex(3, 5)]]
        s = [[comp.Complex(-1, -1)], [comp.Complex(-1, -2)],
             [comp.Complex(-1, -3)], [comp.Complex(-3, -5)]]
        p = Matrix.inverse(v1)
        for i in range(len(p)):
            self.assertEqual(s[i][0].real, p[i][0].real)
            self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_transpose(self):
        m = [[comp.Complex(6, -3), comp.Complex(2, 12), comp.Complex(0, -19)], [
            comp.Complex(0, 0), comp.Complex(5, 2.1), comp.Complex(17, 0)], [
            comp.Complex(1, 0), comp.Complex(2, 5), comp.Complex(3, -4)]]
        s = [[comp.Complex(6, -3), comp.Complex(0, 0), comp.Complex(1, 0)], [
            comp.Complex(2, 12), comp.Complex(5, 2.1), comp.Complex(2, 5)], [
            comp.Complex(0, -19), comp.Complex(17, 0), comp.Complex(3, -4)]]
        p = Matrix.transpose(m)
        for i in range(len(p)):
            for j in range(len(p[0])):
                self.assertEqual(s[i][0].real, p[i][0].real)
                self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_conjugate(self):
        m = [[comp.Complex(6, -3), comp.Complex(2, 12), comp.Complex(0, -19)], [
            comp.Complex(0, 0), comp.Complex(5, 2.1), comp.Complex(17, 0)], [
            comp.Complex(1, 0), comp.Complex(2, 5), comp.Complex(3, -4)]]
        s = [[comp.Complex(6, 3), comp.Complex(2, -12), comp.Complex(0, 19)], [
            comp.Complex(0, 0), comp.Complex(5, -2.1), comp.Complex(17, 0)], [
            comp.Complex(1, 0), comp.Complex(2, -5), comp.Complex(3, 4)]]
        p = Matrix.conjugate(m)
        for i in range(len(p)):
            for j in range(len(p[0])):
                self.assertEqual(s[i][0].real, p[i][0].real)
                self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_product(self):
        v1 = [[comp.Complex(1, 0), comp.Complex(0, 0)], [
            comp.Complex(1, 0), comp.Complex(0, 0)]]
        v2 = [[comp.Complex(1, 1), comp.Complex(1, 1)], [
            comp.Complex(1, 1), comp.Complex(1, 1)]]
        s = [[comp.Complex(1, 1), comp.Complex(1, 1)], [
            comp.Complex(1, 1), comp.Complex(1, 1)]]
        p = Matrix.matrixProduct(v1, v2)
        for i in range(len(p)):
            for j in range(len(p[0])):
                self.assertEqual(s[i][0].real, p[i][0].real)
                self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_adjoint(self):
        m = [[comp.Complex(6, -3), comp.Complex(2, 12), comp.Complex(0, -19)], [
            comp.Complex(0, 0), comp.Complex(5, 2.1), comp.Complex(17, 0)], [
            comp.Complex(1, 0), comp.Complex(2, 5), comp.Complex(3, -4)]]
        s = [[comp.Complex(6, 3), comp.Complex(0, 0), comp.Complex(1, 0)], [
            comp.Complex(2, -12), comp.Complex(5, -2.1), comp.Complex(2, -5)], [
            comp.Complex(0, 19), comp.Complex(17, 0), comp.Complex(3, 4)]]
        p = Matrix.adjoint(m)
        for i in range(len(p)):
            for j in range(len(p[0])):
                self.assertEqual(s[i][0].real, p[i][0].real)
                self.assertEqual(s[i][0].imag, p[i][0].imag)

    def test_matrix_norm(self):
        m = [[comp.Complex(3, 0), comp.Complex(5, 0)], [
            comp.Complex(2, 0), comp.Complex(3, 0)]]
        s =  math.sqrt(47)
        p = Matrix.norm(m)
        self.assertEqual(s,p)

    def test_matrix_distance(self):
        pass

    def test_matrix_unitary(self):
        pass

    def test_matrix_hermitian(self):
        m = [[comp.Complex(5, 0), comp.Complex(4, 5), comp.Complex(6, -16)], [
            comp.Complex(4, -5), comp.Complex(13, 0), comp.Complex(7, 0)], [
            comp.Complex(6, 16), comp.Complex(7, 0), comp.Complex(-2.1, 0)]]
        s = True
        p = Matrix.hermitian(m)
        self.assertEqual(s,p)

    def test_matrix_tensorProduct(self):
        pass


if __name__ == '__main__':
    unittest.main()
