tries = 0

while tries != 5:
    angka1 = input("Masukkan angka pertama :")
    angka2 = input("Masukkan angka kedua :")
    kalkulator = input("Silahkan masukkan operasi yang ingin dilakukan (+), (-), (*), atau (/) :")
    perkalian = int(angka1) * int(angka2)
    pembagian = int(angka1) / int(angka2)
    penjumlahan = int(angka1) + int(angka2)
    pengurangan = int(angka1) - int(angka2)
    
    if kalkulator == "+" : print(f'Hasilnya adalah : {penjumlahan}')
    elif kalkulator == "-" : print(f'Hasilnya adalah :{pengurangan}')
    elif kalkulator == "*" : print(f'Hasilnya adalah : {perkalian}')
    elif kalkulator == "/" : print(f'Hasilnya adalah : {pembagian}')
    tries += 1