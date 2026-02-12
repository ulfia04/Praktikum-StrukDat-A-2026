#class person
class person:
    def __init__(self, nama, jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur
    
#class karyawan turunan dari person
class karyawan(person):
    def __init__(self, nama, jenis_kelamin, umur, gaji):
        super().__init__(nama, jenis_kelamin, umur)
        self._gaji = gaji
    
    def get_gaji(self):
        return self.get_gaji
    
    def self_gaji(self, gaji_baru):
        self._gaji = gaji_baru

#class rekening
class rekening:
    def __init__(self, no_rekening, pin)
        self.no_rekening = no_rekening
        self.__pin = pin
    
    def get_pin(self):
        return self.__pin
    def set_pin(self, pin_baru):
        self.__pin = pin_baru

#buat 1 objek tiap class
    p = person("faniya", "perempuan", 10)
    print("nama", p.nama)

    P_karyawan = karyawan("yanto", "laki-laki", 20, 500000)
    print("gaji", P_karyawan.get_gaji())

    p_rekening = rekening("123456789", "123456")
    print("pin", p_rekening)


    
