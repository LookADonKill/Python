print("Key and Value Dictionary")
tries = 0
murid = {}

while tries != 5:
    x = input("Masukkan key yang ingin ditambahkan :")
    y = input("Masukkan value yang ingin ditambahkan :")
    print("============================================")
    murid[x] = y
    tries += 1
    
    for key, value in murid.items():
        print(f'{key} : {value}')
