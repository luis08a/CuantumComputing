
# Quantum Computing

In order to understand and improve the knowledge about the insteresting world of quantum physics and computing was built a library capable of make simulations about quantum mechanics.

### Library description
---
This is a library made to make simulations and try to understand how the quantum mechanics works. It has :
The complex numbers and its operations, like the sum, product, divition or the convertion between cartesian and polar representation.
The abstraction of a complex vector space,whit complex vectors and matrices and their operations, such as scalar product, the addition between matrices and vector and more.
The Leap from Classical to Quantum, with a few simulations showing how classic and quantum dynamic systems work

---
### Library content. 
---
- Complex object
> You must create an complex object to perform the operations covered in the libarary. This object has two attributes, a real part an imaginary part.
- Complex lirary operations
> Operations with complex numbers:
> - The conjugate of a complex number.
> - Addition between two complex numbers.
> - Difference between two complex numbers.
> - Product between two complex numbers.
> - Division between two complex numbers.
>  - The phase (or angle in polar representation).
>  - The modulus o magnitude (in polar representation).
>  - The conversion among polar and cartesian representation of complex numbers.

> Operations with complex matrices:
> - Addition between two complex matrices.
> - Inverse of a complex matrix.
> - Difference between two complex numbers.
> - Matrix scalar product.
> - Product between two complex matrices.
> - Matrix tranpose.
> - Matrix adjoint.
> - Matrix conjugate.
> - Matrix norm.
> - Distance between vectors and matrices.
> - Show if the matrix is Hermitian.
> - Show if the matrix is Unitary.
> - The tensor product of tow matrices.
- Simulations
 > - Classical Deterministic Systems. A simple simulation with a matrix that theterminates the way that the system evolves over time and an initial state.
 > - Probabilistc systems.
 >  - Quantum systems.

Implementation Sample
```python
class  Complex:

def  __init__(self, real, imaginary):
	self.real = real
	self.imag = imaginary

def  conjugate(self):
	return Complex(self.real, -self.imag)
...
...
...
```
---
## How to use the project.
 To use the project:
 - Go to the src folder
 - Open a windows or linux terminal
 - Type  `py` and in the interactive python shell import the module file `import 'module'`
 - Interact with the functionality of the module.
 
 To test the project.
 - Go to the src folder
  - Open a windows shell or a linux terminal
  - Run the `TestComplex.py`file: `py -m TestComplex`

Use sample
```console
user@pc:~$ python -m TestComplexNumbers

```
Test implementation sample
```python
class  TestComplex(unittest.TestCase):

def  test_ComplexConjugate(self):

	i = comp.Complex(0,0)

	self.assertEqual(0,i.imag)
...
...
...
...
if __name__ ==  '__main__':

	unittest.main()
```

---

## Which tools i used to create the library
- Python3
