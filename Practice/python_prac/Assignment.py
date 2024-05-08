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

# Example usage
num = RationalNumber(4, 6)
num.simplify()
print(num)  # Output: 2/3