#test.py
from colorama import Fore, Back, Style, init

# Inisialisasi colorama untuk Windows
init()

print(Fore.RED + 'Teks Merah')
print(Fore.GREEN + 'Teks Hijau')
print(Fore.BLUE + Back.YELLOW + 'Teks Biru, Bg Kuning')
print(Style.RESET_ALL + 'Kembali Normal')