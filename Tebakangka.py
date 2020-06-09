angka = 13
tries = 0
while tries != 5:
    tebak = int(input("Tebak angka dari 1-30 :"))
    if tebak > angka: print("Kebesaran")
    elif tebak < angka: print("Kekecilan")
    elif tebak == angka: 
        print("Benar")
        break
    tries += 1
    