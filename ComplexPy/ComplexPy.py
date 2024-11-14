import math
from decimal import Decimal

class complexNumber():
    def __init__(self, real, imag):
        """
        Initialize a complex number using real and imaginary parts.
        Using Decimal for higher precision.

        Arguments:
        real -- The real part of the complex number.
        imag -- The imaginary part of the complex number.

        Example:
        ```
        num = complexNumber(3, 4)
        print(num.real)  # Will print 3
        print(num.imag)  # Will print 4
        ```
        """
        self.real = Decimal(real)
        self.imag = Decimal(imag)

    def toString(self):
        """
        Convert a complex number into a readable format (a + bi).

        Example:
        ```
        number = complexNumber(7, 8)
        print(number.toString())  # Will print "7 + 8i"
        number2 = complexNumber(3, -4)
        print(number2.toString())  # Will print "3 - 4i"
        ```
        """
        if self.imag != 0:
            return f"{self.real} {'+' if self.imag > 0 else '-'} {abs(self.imag)}i"
        else:
            return f"{self.real}"

    def add(self, num):
        """
        Adds two complex numbers.

        Arguments:
        num -- The number being added to the input.

        Example:
        ```
        num1 = complexNumber(3, 4)
        num2 = complexNumber(1, 2)
        result = num1.add(num2)
        print(result.toString())  # Will print "4 + 6i"
        ```
        """
        return complexNumber(self.real + num.real, self.imag + num.imag)
    sum = add

    def sub(self, num):
        """
        Subtracts two complex numbers.

        Arguments:
        num -- The number being subtracted to the input.

        Example:
        ```
        num1 = complexNumber(7, 8)
        num2 = complexNumber(3, 4)
        result = num1.sub(num2)
        print(result.toString())  # Will print "4 + 4i"
        ```
        """
        return complexNumber(self.real - num.real, self.imag - num.imag)
    subtract = sub
    difference = sub

    def mul(self, num):
        """
        Multiplies two complex numbers.

        Arguments:
        num -- The number the input is being multiplied by.

        Example:
        ```
        num1 = complexNumber(1, 2)
        num2 = complexNumber(3, 4)
        result = num1.mul(num2)
        print(result.toString())  # Will print "-5 + 10i"
        ```
        """
        return complexNumber(self.real * num.real - self.imag * num.imag, self.real * num.imag + self.imag * num.real)
    multiply = mul
    product = mul
    scale = mul

    def div(self, num):
        """
        Divides two complex numbers.

        Arguments:
        num -- The number the input is being divided by.

        Example:
        ```
        num1 = complexNumber(3, 2)
        num2 = complexNumber(1, 1)
        result = num1.div(num2)
        print(result.toString())  # Will print "2.5 - 0.5i"
        ```
        """
        return complexNumber((self.real * num.real + self.imag * num.imag)/(num.real ** 2 + num.imag ** 2), 
                             (self.imag * num.real - self.real * num.imag)/(num.real ** 2 + num.imag ** 2))
    divide = div
    quotient = div

    def pow(self, num):
        """
        Raises one complex number to another.

        Arguments:
        num -- The number to raise the input to.

        Example:
        ```
        num1 = complexNumber(1, 1)
        num2 = complexNumber(2, 0)
        result = num1.pow(num2)
        print(result.toString())  # Will print "0.0 + 1.4142135623730951i"
        ```
        """
        r = math.sqrt(self.real ** 2 + self.imag ** 2)
        t = math.atan2(self.imag, self.real)
        exp_modulus = math.exp(num.real * math.log(r) - num.imag * t)
        expCos = math.cos(num.real * t + num.imag * math.log(r))
        expSin = math.sin(num.real * t + num.imag * math.log(r))
        return complexNumber(exp_modulus * expCos, exp_modulus * expSin)
    exponentiate = pow
    exp = pow

    def pow2(self, base, exp):
        """
        Efficient exponentiation by squaring for large exponents.

        Arguments:
        base -- The base to exponentiate.
        exp -- The exponent.

        Example:
        ```
        result = num.pow2(3, 4)
        print(result)  # Will print 81
        ```
        """
        if exp == 0:
            return Decimal(1)
        elif exp % 2 == 0:
            half = self.exp_by_squaring(base, exp // 2)
            return half * half
        else:
            return base * self.exp_by_squaring(base, exp - 1)
    exponentiate2 = pow2
    exp2 = pow2

    def sqrt(self, k=0):
        """
        Takes the square root of a complex number.

        Arguments:
        k -- The index of the root.

        Example:
        ```
        num = complexNumber(3, 8)
        print(num.sqrt().toString())  # Will print "2.3038850997677716 + 1.5191729832155236i"
        print(num.sqrt(1).toString())  # Will print "-2.3038850997677716 - 1.5191729832155234i"
        ```
        """
        r = math.sqrt(self.real ** 2 + self.imag ** 2)
        t = math.atan2(self.imag, self.real)
        cos = math.cos((t + 2 * k * math.pi)/2)
        sin = math.sin((t + 2 * k * math.pi)/2)
        return complexNumber(math.sqrt(r), 0).mul(complexNumber(cos, sin))
    square_root = sqrt

    def nroot(self, n, k=0):
        """
        Takes the nth root of a complex number.

        Arguments:
        n -- The root degree.
        k -- The index of the root.

        Example:
        ```
        num = complexNumber(3, 8)
        print(num.nroot(3).toString())  # Will print "1.879758450168867 + 0.8036462937138271i"
        print(num.nroot(3, 1).toString())  # Will print "-1.635857331097818 + 1.2260954239677901i"
        ```
        """
        r = math.sqrt(self.real ** 2 + self.imag ** 2)
        t = math.atan2(self.imag, self.real)
        cos = math.cos((t + 2 * k * math.pi)/n)
        sin = math.sin((t + 2 * k * math.pi)/n)
        return complexNumber(r ** (1/n), 0).mul(complexNumber(cos, sin))
    nth_root = nroot

    def abs(self):
        """
        Returns the absolute value (or modulus) of a complex number.

        Example:
        ```
        num = complexNumber(3, 4)
        print(num.abs().toString())  # Will print "5.0"
        ```
        """
        return complexNumber(math.sqrt(self.real ** 2 + self.imag ** 2), 0)
    absolute_value = abs
    modulus = abs
    mod = abs

    def conj(self):
        """
        Returns the conjugate of a complex number.

        Example:
        ```
        num = complexNumber(3, 4)
        print(num.conj().toString())  # Will print "3 - 4i"
        ```
        """
        return complexNumber(self.real, -self.imag)
    conjugate = conj

    def arg(self):
        """
        Returns the argument (angle) of a complex number.

        Example:
        ```
        num = complexNumber(3, 4)
        print(num.arg().toString())  # Will print "0.9272952180016122"
        ```
        """
        return complexNumber(math.atan2(self.imag, self.real), 0)
    argument = arg

    def ln(self):
        """
        Returns the natural logarithm of a complex number.

        Example:
        ```
        num = complexNumber(3, 4)
        print(num.ln().toString())  # Will print "1.6094379124341003 + 0.9272952180016122i"
        ```
        """
        modulus = math.sqrt(self.real ** 2 + self.imag ** 2)
        arg = math.atan2(self.imag, self.real)
        return complexNumber(math.log(modulus), arg)
    log = ln
