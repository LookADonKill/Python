murid = {}

nama = input("Masukkan nama anda :")
NIS = int(input("Masukkan NIS anda :"))
Umur = int(input("Masukkan Umur anda :"))
Tinggi = int(input("Masukkan Tinggi anda :"))
Berat = int(input("Masukkan Berat anda :"))

murid["Nama"] = nama
murid["NIS"] = NIS
murid["Umur"] = Umur
murid["Tinggi Badan"] = Tinggi
murid["Berat Badan"] = Berat

for key, value in murid.items():
    if key == "Tinggi Badan":
        print(f'{key} : {value} cm')
    elif key == "Berat Badan":
        print(f'{key} : {value} kg')
    elif key == "Umur":
        print(f'{key} : {value} tahun')
    elif key == "NIS":
        print(f'{key} : {value}')
    elif key == "Nama":
        print(f'{key} : {value}')