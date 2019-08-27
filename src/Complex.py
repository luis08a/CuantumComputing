import math


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def phase(self):
        return math.atan(self.imag/self.real)

    def modulus(self):
        return math.sqrt(math.pow(self.real, 2) + math.pow(self.imag, 2))

    def inverse(self):
        self.real = -self.real
        self.imag = -self.imag

    @staticmethod
    def add(a, b):
        return Complex(a.real + b.real, a.imag + b.imag)

    @staticmethod
    def mult(a, b):
        real = a.real*b.real - a.imag*b.imag
        imag = a.real*b.imag + b.real*a.imag
        return Complex(real, imag)

    @staticmethod
    def dif(a, b):
        return Complex(a.real - b.real, a.imag - b.imag)

    @staticmethod
    def div(a, b):
        real = (a.real*b.real + a.imag*b.imag) / \
            (math.pow(a.imag, 2)+math.pow(b.imag, 2))
        imag = (a.imag*b.real - a.real*b.imag) / \
            (math.pow(a.imag, 2)+math.pow(b.imag, 2))
        return Complex(real, imag)

    @staticmethod
    def cartesianToPolar(complex):
        return complex.modulus(), complex.phase()

    @staticmethod
    def polarToCartesian(module, phase):
        return Complex(module*math.cos(phase), module*math.sin(phase))
