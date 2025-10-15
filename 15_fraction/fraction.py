class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        divisor = gcd(numerator, denominator)
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor
    
    # Getters
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    # Setters
    @numerator.setter
    def numerator(self, value):
        # TODO
        self._numerator = value // gcd(value, self.denominator)

    
    @denominator.setter
    def denominator(self, value):
        # TODO
        if value == 0:
            print("Incorrect input: denominator cannot be zero")
            self._denominator = 1
        else:
            self._denominator = value

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __floordiv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return n // d
    
    def __mod__(self, other):
        return self - other * (Fraction(self // other, 1))
    
    def __pow__(self, other):
        exp = other.numerator / other.denominator
        return (self.numerator ** exp) / (self.denominator ** exp)
    
    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)
    
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    
    def __le__(self, other):
        return self.__cmp__(other) <= 0
    
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    
    def __ne__(self, other):
        return self.__cmp__(other) != 0
    
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    
    def __ge__(self, other):
        return self.__cmp__(other) >= 0
    
    def __cmp__(self, other):
        temp = self - other
        if temp.numerator < 0:
            return -1
        elif temp.numerator > 0:
            return 1
        else:
            return 0
    
def gcd(n, d):
    gcd = 1
    k = 1

    while k <= n and k <= d:
        if n % k == 0 and d % k == 0:
            gcd = k
        
        k += 1
    
    return gcd
    
f1 = Fraction(2, 3)
print(f1.numerator)
print(f1.denominator)

print(f1)

f1.numerator = 7
print(f1)

f2 = Fraction(3, 7)

print(f"{f1} * {f2} = {f1 * f2}") # f1 * f2 -> f1.__mul__(f2)
print(f"{f1} < {f2} is {f1 < f2}")
print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
print(f"{f1} / {f2} = {f1 / f2}")
print(f"{f1} // {f2} = {f1 // f2}")
print(f"{f1} % {f2} = {f1 % f2}")
print(f"{f1} ** {f2} = {f1 ** f2}")
print(f"{f1} <= {f2} is {f1 <= f2}")
print(f"{f1} == {f2} is {f1 == f2}")
print(f"{f1} != {f2} is {f1 != f2}")
print(f"{f1} > {f2} is {f1 > f2}")
print(f"{f1} >= {f2} is {f1 >= f2}")