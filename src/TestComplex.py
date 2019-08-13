import unittest
import complexNumLib as comp
import math

class TestComplex(unittest.TestCase):
    
    def test_ComplexConjugate(self):
        i = comp.Complex(0,0)
        self.assertEqual(0,i.imag)
        i = comp.Complex(0,8)
        self.assertEqual(8,i.imag)
        i = comp.Complex(0,-8)
        self.assertEqual(-8,i.imag)
    def test_ComplexModulus(self):
        i = comp.Complex(0,0)
        self.assertEqual(0,i.modulus())

        i = comp.Complex(3,4)
        self.assertEqual(5,i.modulus()) 

        i = comp.Complex(-3,-4)
        self.assertEqual(5,i.modulus()) 
    def test_ComplexPhase(self):
        pass
    def test_ComplexSum(self):
        a = comp.Complex(0,0)
        b = comp.Complex(0,0)
        s = comp.Complex.add(a,b)
        self.assertAlmostEqual(0,s.real)
        self.assertAlmostEqual(0,s.imag)

        a = comp.Complex(3,0)
        b = comp.Complex(5,0)
        s = comp.Complex.add(a,b)
        self.assertAlmostEqual(8,s.real)
        self.assertAlmostEqual(0,s.imag)

        a = comp.Complex(0,8)
        b = comp.Complex(0,4)
        s = comp.Complex.add(a,b)
        self.assertAlmostEqual(0,s.real)
        self.assertAlmostEqual(12,s.imag)

        a = comp.Complex(1,-6)
        b = comp.Complex(20,2)
        s = comp.Complex.add(a,b)
        self.assertAlmostEqual(21,s.real)
        self.assertAlmostEqual(-4,s.imag)
    def test_ComplexProduct(self):
        a = comp.Complex(0,0)
        b = comp.Complex(0,0)
        s = comp.Complex.mult(a,b)
        self.assertAlmostEqual(0,s.real)
        self.assertAlmostEqual(0,s.imag)
    def test_ComplexDiv(self):
        a = comp.Complex(0,0)
        b = comp.Complex(0,0)
        try:
            s = comp.Complex.div(a,b)
        except ZeroDivisionError:
            return True
        a = a = comp.Complex(89,34)
        try:
            s = comp.Complex.div(a,b)
        except ZeroDivisionError:
            return True
    def test_conversion(self):
        pass

if __name__ == '__main__':
        unittest.main()