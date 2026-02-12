# Contoh operator perbandingan
print(15 > 3)   # True
print(20 != 20) # False
print(7 <= 9)   # True

# Variabel baru
m = 123
n = 456

if m > n:
    print("m lebih besar dari n")
else:
    print("m tidak lebih besar dari n")  # akan dicetak karena kondisi False

# Evaluasi nilai boolean dengan fungsi bool()
print(bool("python"))  # True karena string tidak kosong
print(bool(""))        # False karena string kosong

# Hampir semua nilai dianggap True
print(bool("hello"))
print(bool(2026))
print(bool([4, 5, 6]))

# Fungsi yang mengembalikan boolean
def cekStatus():
    return False

print(cekStatus())  # mencetak False

# isinstance untuk cek tipe data
y = 3.14159
print(isinstance(y, float))  # True