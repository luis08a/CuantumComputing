# from sys import stdin

# def adition(n1,n2):
#     newNum = []
#     newNum[0] = n1[0]+n2[0]
#     newNum[1] = n1[1]+n2[1]
#     return newNum
    
# def main():
#     fstNum = stdin.readline().split().strip();
#     sndNum = stdin.readline().split().sptrip();
    

# main()
import math
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    @staticmethod
    def add(a, b):
        return Complex(a.real + b.real, a.imag + b.imag)
    @staticmethod    
    def mult(a, b):
        real = a.real*b.real - a.imag*b.imag
        imag = a.real*b.imag + b.real*a.imag
        return Complex(real,imag)
    @staticmethod
    def dif(a, b):
        return Complex(a.real - b.real, a.imag - b.imag)
    @staticmethod
    def div(a, b):
        real = (a.real*b.real + a.imag*b.imag)/(math.pow(a.imag)+math.pow(b.imag))
        imag = (a.imag*b.real - a.real*b.imag)/(math.pow(a.imag)+math.pow(b.imag))
        return Complex(real,imag)

    def phase(self):
        return math.atan(self.imag/self.real)
    def modulus(self):
        return math.sqrt(math.pow(self.real,2) + math.pow(self.imag,2))