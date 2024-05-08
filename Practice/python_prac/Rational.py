import math

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def add(self, fraction):
        self.numerator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        self.denominator = self.denominator * fraction.denominator
        self.simplify()

    def multiply(self, fraction):
        self.numerator = self.numerator * fraction.numerator
        self.denominator = self.denominator * fraction.denominator
        self.simplify()

num = RationalNumber(1, 2)
num.simplify()
print(num)  

num2 = RationalNumber(-3, 8)
num2.simplify()
print(num2)

num3 = RationalNumber(4, 6)
num3.simplify()
print(f"Simplified form  of 4/6 = {num3}")

num4 = RationalNumber(1, 2)
num4.add(num2)
print(f"Sum of 1/2 and -3/8 = {num4}")

num5 = RationalNumber(1, 2)
num5.multiply(num2)
print(f"Product of 1/2 and -3/8 = {num5}")