def luas(x,y):
    return(x*y)

def volume(x,y):
    return(x*y)

panjang = int(input("Masukkan panjang dari persegi :"))
lebar = int(input("Masukkan lebar dari persegi :"))
tinggi = int(input("Masukkan tinggi dari persegi :"))

hasil = luas(panjang, lebar)

hasil_akhir = volume(hasil,tinggi)

print(hasil_akhir)