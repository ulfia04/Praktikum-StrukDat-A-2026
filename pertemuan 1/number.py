a = 10
b = 987654321
c = -12345
print(type(a))
print(type(b))
print(type(c))

# Contoh float
p = 6.28
q = -0.75
r = 18.0
print(type(p))
print(type(q))
print(type(r))

# Contoh complex
x = 5 + 2j
y = -3j
z = 7 - 4j
print(type(x))
print(type(y))
print(type(z))

# Tipe konversi
num1 = 50      # int
num2 = 7.89    # float
num3 = 3 + 4j  # complex

a = float(num1)   # int -> float
b = int(num2)     # float -> int
c = complex(num1) # int -> complex
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random numbers
import random

print(random.randrange(10, 21))  # angka random antara 10 sampai 20
print(random.random())            # angka random float antara 0.0 sampai 1.0