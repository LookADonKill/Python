import random

angka = random.randint(1,31)
tebak = ""
while tebak != angka:
    tebak = int(input("Tebak angka dari 1-30 :"))
    if tebak > angka: print("Kebesaran")
    elif tebak < angka: print("Kekecilan")
    elif tebak == angka: 
        print("Benar")