print("PAYMENT COMPUTATION FOR EMPLOYEE")
print("--------------------------------")
angka = 10
def gaji(x,y):
    if Jam > angka:
        return(200 + (x * y))
    elif Jam < angka:
        return(x * y)

Jam = int(input("Enter work hours :"))
Rate = int(input("Enter work rate :"))
Hasil = gaji(Jam, Rate)

print(Hasil)