nama = input("Masukkan nama dari bunga yang ingin anda beli :")
jumlah = int(input("Masukkan jumlah kelopak dari bunga yang ingin anda beli :"))
harga = float(input("Masukkan range harga dari bunga yang ingin dicari :"))

class Bunga:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        print(f'Bunga yang ingin dibeli adalah {self.nama} dengan jumlah kelopak sebanyak {self.jumlah} buah juga memiliki harga Rp {self.harga}')
    
    def x(self, nama2):
        self.nama = nama2

    def y(self, jumlah2):
        self.jumlah = jumlah2
        
    def z(self, harga2):
        self.harga = harga2
    
    def nama1(self):
        return(self.nama)
    
    def harga1(self):
        return(self.harga)
    
    def jumlah1(self):
        return(self.jumlah)

nama2 = input("Masukkan nama lain dari bunga tersebut :")
jumlah2 = int(input("Masukkan variasi lain dari jumlah kelopaknya :"))
harga2 = float(input("Masukkan harga dari bunga yang ingin dicari :"))
Flower = Bunga(nama, jumlah, harga)
Flower.x(nama2)
Flower.y(jumlah2)
Flower.z(harga2)
nama = Flower.nama1()
jumlah = Flower.jumlah1()
harga = Flower.harga1()
print(nama, jumlah, harga)