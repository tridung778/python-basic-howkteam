from decimal import *
from fractions import Fraction

getcontext().prec = 30

a = 1234
print(a)
print(type(a))

b = Decimal(10) / Decimal(3)
print(b)
print(type(b))

# phân số
c = Fraction(10, 3)
print(c)
print(type(c))

# số phức
d = complex(10, 3)
print(d)
# lấy phần thực
print(d.real)
# lấy phần ảo
print(d.imag)
print(type(d))
