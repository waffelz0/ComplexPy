import math

class complexNumber():
    def __init__(self, real, imag):
        """
        Initialize a complex number using real and imaginary parts.

        Arguments:
        ``real``: The real part of the complex number.
        ``imag``: The imaginary part of the complex number.
        
        Example:
        ```
        number = complexNumber(1, 4)
        print(number.toString()) # Will print "1 + 4 i"
        ```
        """

        self.real = real
        self.imag = imag

    def toString(self):
        """
        Convert a complex number into a readable format (a + bi).

        Example:
        ```
        number = complexNumber(7, 8)
        print(number.toString()) # Will print "7 + 8 i"
        ```
        """

        if self.imag != 0:
            return(f"{self.real}{" + " if self.imag > 0 else " - "}{abs(self.imag)} i")
        else:
            return(f"{self.real}")

    def add(self, num):
        """
        Adds two complex numbers.

        Arguments:
        ``num``: The number being added to the input.
        """

        return complexNumber(self.real + num.real, self.imag + num.imag)
    sum = add

    def sub(self, num):
        """
        Subtracts two complex numbers.

        Arguments:
        ``num``: The number being subtracted to the input.
        """

        return complexNumber(self.real - num.real, self.imag - num.imag)
    subtract = sub
    difference = sub

    def mul(self, num):
        """
        Multiplies two complex numbers.

        Arguments:
        ``num``: The number the input is being multiplied by.
        """

        return complexNumber(self.real * num.real - self.imag * num.imag, self.real * num.imag + self.imag * num.real)
    multiply = mul
    product = mul
    scale = mul
    
    def div(self, num):
        """
        Divides two complex numbers.

        Arguments:
        ``num``: The number the input is being divided by.
        """

        return complexNumber((self.real * num.real + self.imag * num.imag)/(num.real ** 2 + num.imag ** 2), (self.imag * num.real - self.real * num.imag)/(num.real ** 2 + num.imag ** 2))
    divide = div
    quotient = div

    def pow(self, num):
        """
        Raises one complex number to another.

        Arguments:
        ``num``: The number to raise the input to.
        """

        r = math.sqrt(self.real ** 2 + self.imag ** 2)
        t = math.atan2(self.imag, self.real)
        exp_modulus = math.exp(num.real * math.log(r) - num.imag * t)
        expCos = math.cos(num.real * t + num.imag * math.log(r))
        expSin = math.sin(num.real * t + num.imag * math.log(r))
        return complexNumber(exp_modulus * expCos, exp_modulus * expSin)
    exponentiate = pow

    def sqrt(self, k=0):
        """
        Takes the square root of a complex number.

        Arguments:
        ``k``: The index of the root.

        Example:

        ```
        number = complexNumber(3, 8)
        print(number.sqrt().toString()) # Will print "2.3038850997677716 + 1.5191729832155236 i"
        print(number.sqrt(1).toString()) # Will print "-2.3038850997677716 - 1.5191729832155234 i"
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
        ``k``: The index of the root.

        Example:

        ```
        number = complexNumber(3, 8)
        print(number.nroot(3).toString()) # Will print "1.879758450168867 + 0.8036462937138271 i"
        print(number.nroot(3, 1).toString()) # Will print "-1.635857331097818 + 1.2260954239677901 i"
        print(number.nroot(3, 2).toString()) # Will print "-0.2439011190710484 - 2.029741717681617 i"
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
        """

        return complexNumber(math.sqrt(self.real ** 2 + self.imag ** 2), 0)
    absolute_value = abs
    modulus = abs
    mod = abs
    
    def conj(self):
        """
        Returns the conjugate of a complex number.
        """

        return complexNumber(self.real, -self.imag)
    conjugate = conj

    def arg(self):
        """
        Returns the argument of a complex number.
        """

        return complexNumber(math.atan2(self.imag, self.real), 0)
    argument = arg

    def ln(self):
        """
        Returns the natural logarithm of a complex number.
        """
        
        return complexNumber(math.log(self.mod().real), self.arg().real)
    natural_log = ln
    natural_logarithm = ln

    def log(self, base):
        """
        Returns the general logarithm of of a number.

        Arguments:
        ``base``: The base of the logarithm.
        """

        return self.ln().div(base.ln())
    logarithm = log
    general_log = log

    def eq(self, num):
        """
        Checks if a number is equal to another.

        Arguments:
        ``num``: The number to compare to.
        """

        return self.real == num.real and self.imag == num.imag
    equals = eq

    def le(self, num):
        """
        Checks if a number is less than another.

        Arguments:
        ``num``: The number to compare to.
        """

        return self.mod().real < num.mod().real
    less = le
    less_than = le

    def gr(self, num):
        """
        Checks if a number is greater than another.

        Arguments:
        ``num``: The number to compare to.
        """

        return self.mod().real > num.mod().real
    greater = gr
    greater_than = gr

    def leeq(self, num):
        """
        Checks if a number is less than or equal to another.

        Arguments:
        ``num``: The number to compare to.
        """

        return self.mod().real <= num.mod().real
    less_than_or_equals = leeq

    def greq(self, num):
        """
        Checks if a number is greater than or equal to another.

        Arguments:
        ``num``: The number to compare to.
        """

        return self.mod().real >= num.mod().real
    greater_than_or_equals = greq

    def sin(self):
        """
        Returns the sine of a complex number.
        """

        return complexNumber(math.sin(self.real) * math.cosh(self.imag), math.cos(self.real) * math.sinh(self.imag))
    sine = sin

    def cos(self):
        """
        Returns the cosine of a complex number.
        """

        return complexNumber(math.cos(self.real) * math.cosh(self.imag), -math.sin(self.real) * math.sinh(self.imag))
    cosine = cos

    def tan(self):
        """
        Returns the tangent of a complex number.
        """

        return self.sin().div(self.cos())
    tangent = tan