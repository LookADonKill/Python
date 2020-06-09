import random

while True:
    Pilihan = random.randint(0,2)
    Acakan = ['Rock', 'Paper', 'Scissors']
    Isi = Acakan[Pilihan]
    hasil = input("Rock, Paper, or Scissors ?")

    if hasil == 'Rock' and Isi == 'Rock':
        print("TIE")
    elif hasil == 'Rock' and Isi == 'Scissors':
        print("YOU WIN")
    elif hasil == 'Rock' and Isi == 'Paper':
        print("YOU LOSE")
    elif hasil == 'Paper' and Isi == 'Paper':
        print("TIE")
    elif hasil == 'Paper' and Isi == 'Rock':
        print("YOU WIN")
    elif hasil == 'Paper' and Isi == 'Scissors':
        print("YOU LOSE")
    elif hasil == 'Scissors' and Isi == 'Scissors':
        print("TIE")
    elif hasil == 'Scissors' and Isi == 'Paper':
        print("YOU WIN")
    elif hasil == 'Scissors' and Isi == 'Rock':
        print("YOU LOSE")
    else:
        break