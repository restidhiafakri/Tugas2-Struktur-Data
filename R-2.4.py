class flower:
    def __init__(self,nama, jumlah_kelopak, harga):
        self.nama = nama
        self.jumlah_kelopak = jumlah_kelopak
        self.harga = harga

    def set_nama(self, new_nama):
        self.nama = new_nama

    def set_jumlah_kelopak(self, new_jumlah_kelopak):
        self.nama = new_jumlah_kelopak

    def harga(self, new_harga):
        self.nama = new_harga


flower1 = flower("Kembang_sepatu", 5, 10000)
print("Bunga", flower1.nama, "Memiliki kelopak", flower1.jumlah_kelopak, "Dengan Harga", flower1.harga)
flower1.set_nama("Kembang_sepatu")
print("Bunga", flower1.nama, "Memiliki kelopak", flower1.jumlah_kelopak, "Dengan Harga", flower1.harga)