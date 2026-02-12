# strings
print("rizki putra")        # string dengan kutip ganda
print('rizki putra')        # string dengan kutip tunggal
print("98765")              # string angka

# kutip dalam kutip
print("dia berkata 'oke'")  # kutip tunggal dalam kutip ganda
print('dia berkata "tidak"')# kutip ganda dalam kutip tunggal

# assign string ke variabel
nama = "rizki putra"
print(nama)

# multiline string
alamat = """bandung
jawa barat
indonesia"""
print(alamat)

# alternatif dengan \n
alamat2 = 'bandung\njawa barat\nindonesia'
print(alamat2)

# alternatif dengan 3 kutip tunggal
alamat3 = '''bandung
jawa barat
indonesia'''
print(alamat3)

# string adalah array
a = "rizki"
print(a[0])  # karakter pertama
print(a[1])  # karakter kedua
print(a[2])  # karakter ketiga

# looping string
for x in "rizki":
    print(x)

# panjang string
a = 'rizki putra'
print(len(a))  # menghitung panjang string

# cek string
txt = "teknik komputer universitas bandung"
print("komputer" in txt)  # True karena kata ada

txt2 = "teknik elektro universitas bandung"
if "elektro" in txt2:
    print("ada kata elektro dalam txt2")
else:
    print("tidak ada kata elektro dalam txt2")

# memotong string (slicing)
a = "hidup itu singkat"
print(a[0:5])   # 'hidup'
print(a[6:9])   # 'itu'
print(a[:5])    # dari awal sampai index 4
print(a[6:])    # dari index 6 sampai akhir
print(a[-6:-1]) # karakter ke-6 dari belakang sampai ke-2 dari belakang
print(a[-6:])   # dari karakter ke-6 dari belakang sampai akhir

# ubah string
a = "roti bakar manis"
print(a.upper())  # huruf kapital
b = "ROTI BAKAR MANIS"
print(b.lower())  # huruf kecil
c = "   kopi hitam   "
print(c.strip())  # hapus spasi di awal/akhir
print(a.replace("bakar", "panggang")) # ganti kata
d = "fisika, kimia, biologi"
print(d.split(", "))  # pisahkan string berdasarkan koma dan spasi

# gabung string
a = 'rizki'
b = ' putra'
c = ' santoso'
print(a + b + c)  # gabung string

# format string
ipk = 3.7
txt = "IPK rizki adalah " + str(ipk)
print(txt)

# F-string
ipk2 = 3.9
txt2 = f"IPK rizki adalah {ipk2}"
print(txt2)

# placeholder dan modifier
jumlah = 500
txt = f"Jumlah mahasiswa: {jumlah} orang"
print(txt)

# escape character
txt = "universitas memiliki jurusan \"teknik komputer\" dan \'teknik elektro\'"
print(txt)