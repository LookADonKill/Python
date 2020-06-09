username = "JX25"
password = "Juan2305"

tries = 0

while tries != 3:
    Nama_akun = input("Masukkan username anda :")
    Password = input("Masukkan password :")
    if Nama_akun == username and Password == password :
        print('Selamat datang, Juan Xavier')
        break
    print('Ada kesalahan di username maupun password anda, silahkan dicoba lagi')
    tries += 1