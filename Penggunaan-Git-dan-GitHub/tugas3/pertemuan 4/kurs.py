# kurs.py - Module untuk menyimpan data kurs mata uang

# Dictionary kurs mata uang (IDR ke mata uang asing)
kurs_dict = {
    'USD': 16875,  # 1 USD = 16.875 IDR
    'EUR': 19995,  # 1 EUR = 19.995 IDR
    'SGD': 13360,  # 1 SGD = 13.360 IDR
    'JPY': 109     # 100 JPY = 109 IDR (atau 1 JPY = 1.09 IDR)
}

# Fungsi untuk mendapatkan daftar mata uang yang tersedia
def get_daftar_mata_uang():
    return list(kurs_dict.keys())

# Fungsi untuk mendapatkan kurs
def get_kurs(kode_mata_uang):
    return kurs_dict.get(kode_mata_uang.upper(), None)

# Testing module jika dijalankan langsung
if __name__ == '__main__':
    print('Testing module kurs.py')
    print('Daftar mata uang:', get_daftar_mata_uang())
    print('Kurs USD:', get_kurs('USD'))