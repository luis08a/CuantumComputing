import unittest
import Complex as comp
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
        i = comp.Complex(-1,-1)
        self.assertEqual(math.radians(45),i.phase())
        i = comp.Complex(-1,1)
        self.assertEqual(math.radians(-45),i.phase())
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
        a = comp.Complex(1,3)
        b = comp.Complex(5,3)
        s = comp.Complex.div(a,b)
        self.assertEqual(0.4117647058823529,s.real)
        self.assertEqual(0.35294117647058826,s.imag)
    def test_ComplexConvertion(self):
        i = comp.Complex(3,3)
        self.assertEqual(math.sqrt(18), i.modulus())
        self.assertEqual(math.radians(45),i.phase())
        i = comp.Complex(-3,-3)
        self.assertEqual(math.sqrt(18), i.modulus())
        self.assertEqual(math.radians(45),i.phase())

        p = comp.Complex.polarToCartesian(math.sqrt(18),math.radians(45))
        self.assertAlmostEqual(3,p.real)
        self.assertAlmostEqual(3,p.imag)

if __name__ == '__main__':
        unittest.main()