class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan
    
    def get_info(self):
        print(f"Nama    : {self.nama}")
        print(f"Umur    : {self.umur}")
        print(f"Jurusan : {self.jurusan}")
    
    def set_nama(self, nama_baru):
        self.nama = nama_baru
    
    def set_umur(self, umur_baru):
        self.umur = umur_baru

mhs1 = Mahasiswa("Cournicova", 20, "Pendidikan Teknik Informatika")
mhs2 = Mahasiswa("Afiffah", 19, "Pendidikan Bahasa Inggris")
mhs3 = Mahasiswa("Syailendra", 20, "Pendidikan Dokter")

mhs1.get_info()
print("-"*40)
mhs2.get_info()
print("-"*40)
mhs3.get_info()
print()
mhs2.set_nama("Maharani")
mhs2.set_umur(20)
print("-"*40)
mhs2.get_info()
