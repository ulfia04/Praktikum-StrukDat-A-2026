# konverter.py - Module untuk fungsi konversi mata uang

import kurs

def konversi_idr_ke_asing(jumlah_idr, mata_uang_tujuan):
    """
    Mengkonversi dari IDR ke mata uang asing
    """
    kurs_tujuan = kurs.get_kurs(mata_uang_tujuan)
    if kurs_tujuan is None:
        return None
    
    if mata_uang_tujuan == 'JPY':
        # Khusus JPY karena kurs dalam 100 JPY
        hasil = (jumlah_idr / kurs_tujuan) * 100
    else:
        hasil = jumlah_idr / kurs_tujuan
    
    return round(hasil, 2)

def konversi_asing_ke_idr(jumlah_asing, mata_uang_asal):
    """
    Mengkonversi dari mata uang asing ke IDR
    """
    kurs_asal = kurs.get_kurs(mata_uang_asal)
    if kurs_asal is None:
        return None
    
    if mata_uang_asal == 'JPY':
        # Khusus JPY karena kurs dalam 100 JPY
        hasil = (jumlah_asing / 100) * kurs_asal
    else:
        hasil = jumlah_asing * kurs_asal
    
    return round(hasil, 2)

def format_angka(angka):
    """
    Memformat angka dengan pemisah ribuan
    """
    return f"{angka:,.0f}".replace(',', '.')

# Testing module jika dijalankan langsung
if __name__ == '__main__':
    print('Testing module konverter.py')
    print('1000000 IDR ke USD:', konversi_idr_ke_asing(1000000, 'USD'))
    print('100 USD ke IDR:', konversi_asing_ke_idr(100, 'USD'))