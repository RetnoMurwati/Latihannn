#Pengulangan Hello World! sebanyak 10 kali
angka = 1

#Output
print('====================')
while angka <= 100:
    if angka is 11:
        break
    elif angka <= 9:
        print('| %d. Hello  World!' % angka,   '|')
        angka += 1
    elif angka == 10:
        print('| %d. Hello World!' % angka, '|')
        angka += 1
    else:
        print()
print('====================')
