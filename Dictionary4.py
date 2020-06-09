biodata = {}
murid = []
while True:
    biodata = {}
    nama = input("Masukkan nama anda :")
    umur = int(input("Masukkan umur anda :"))
    tempat = input("Masukkan tempat tinggal anda :")
    yesno = input("Apakah anda masih mau mengisi biodata ?(y/n)")

    biodata["Nama"] = nama
    biodata["Umur"] = umur
    biodata["Tempat Tinggal"] = tempat
    murid.append(biodata)
    
    if yesno == 'y':
        continue

    elif yesno == 'n':
        for dictionary in murid:
            for key,value in dictionary.items():
                print(f'{key} : {value}')
        break


