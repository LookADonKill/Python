nama3 = input("Masukkan nama dari mobil yang ingin anda beli :")
brand3 = input("Masukkan merek dari mobil tersebut :")
garansi3 = int(input("Masukkan lama garansi yang diinginkan untuk mobil tersebut :"))
power3 = int(input("Masukkan banyaknya power yang dimiliki mobil yang diinginkan :"))
warna3 = input("Masukkan warna mobil yang diinginkan :")

class Otomotif:
    def __init__(self, nama, brand, garansi, power, warna):
        self.nama = nama
        self.brand = brand
        self.garansi = garansi
        self.power = power
        self.warna = warna
    
    def info(self):
        print(f'Mobil ini bernama {self.nama} yang bermerek {self.brand} dan memiliki garansi selama {self.garansi} tahun. Mobil ini memiliki power sebanyak {self.power} cc dan biasanya berwarna {self.warna}.')

mobil1 = Otomotif('Mustang', 'Ford', '5 tahun', '3000 cc', 'Biru')
mobil2 = Otomotif('Gallardo', 'Lamborghini', '3 tahun', '2500 cc', 'Hitam')
mobil3 = Otomotif(nama3, brand3, garansi3, power3, warna3)
mobil3.info()