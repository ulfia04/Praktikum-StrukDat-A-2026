# main.py - Program utama konverter mata uang

import kurs
import konverter
from tabulate import tabulate

def tampilkan_tabel_kurs():
    """
    Menampilkan tabel kurs mata uang menggunakan tabulate
    """
    # Menyiapkan data untuk tabel
    tabel_data = []
    for kode, nilai in kurs.kurs_dict.items():
        if kode == 'JPY':
            tabel_data.append([kode, f"{nilai/100:.3f}"])  # JPY per 1 yen
        else:
            tabel_data.append([kode, f"{nilai/1000:.3f}"])  # Dalam ribuan
    
    # Membuat tabel
    headers = ['Kode', 'Kurs (per 1000 IDR)']
    print("\n=== KONVERTER MATA UANG ===")
    print(tabulate(tabel_data, headers=headers, tablefmt='grid'))

def main():
    # Tampilkan tabel kurs
    tampilkan_tabel_kurs()
    
    # Daftar mata uang yang tersedia
    mata_uang_tersedia = ['IDR'] + kurs.get_daftar_mata_uang()
    
    while True:
        try:
            # Input mata uang asal
            dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
            if dari not in mata_uang_tersedia:
                print("Mata uang tidak tersedia!")
                continue
            
            # Input mata uang tujuan
            ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
            if ke not in mata_uang_tersedia:
                print("Mata uang tidak tersedia!")
                continue
            
            # Input jumlah
            jumlah = float(input("Jumlah: "))
            
            # Proses konversi
            if dari == 'IDR' and ke != 'IDR':
                # Konversi IDR ke mata uang asing
                hasil = konverter.konversi_idr_ke_asing(jumlah, ke)
                if hasil is not None:
                    print(f"Rp {konverter.format_angka(jumlah)} = {hasil:.2f} {ke}")
                else:
                    print("Kurs tidak ditemukan!")
                    
            elif dari != 'IDR' and ke == 'IDR':
                # Konversi mata uang asing ke IDR
                hasil = konverter.konversi_asing_ke_idr(jumlah, dari)
                if hasil is not None:
                    print(f"{jumlah:.2f} {dari} = Rp {konverter.format_angka(hasil)}")
                else:
                    print("Kurs tidak ditemukan!")
                    
            elif dari == ke:
                print("Mata uang asal dan tujuan sama!")
                
            else:
                # Konversi antar mata uang asing (via IDR)
                # Step 1: asing ke IDR
                idr = konverter.konversi_asing_ke_idr(jumlah, dari)
                if idr is None:
                    print("Kurs tidak ditemukan!")
                    continue
                
                # Step 2: IDR ke asing tujuan
                hasil = konverter.konversi_idr_ke_asing(idr, ke)
                if hasil is not None:
                    print(f"{jumlah:.2f} {dari} = {hasil:.2f} {ke}")
                else:
                    print("Kurs tidak ditemukan!")
            
            # Tanya apakah ingin lanjut
            lanjut = input("\nKonversi lagi? (y/n): ").lower()
            if lanjut != 'y':
                print("Terima kasih telah menggunakan konverter mata uang!")
                break
                
        except ValueError:
            print("Error: Masukkan angka yang valid!")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan!")
            break

if __name__ == '__main__':
    main()