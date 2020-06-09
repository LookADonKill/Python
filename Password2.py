username = "JX25"
password = "Juan2305"

Nama_akun = input("Masukkan username anda :")
Password = input("Masukkan password :")

while Nama_akun != username or Password != password:
    print('Ada kesalahan di username maupun password anda, silahkan dicoba lagi')
    Nama_akun = input("Masukkan username anda :")
    Password = input("Masukkan password :")
print('Selamat datang, Juan Xavier')