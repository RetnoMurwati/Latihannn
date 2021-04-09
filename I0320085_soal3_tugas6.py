print("----- Menentukan Bilangan Prima -----")
for i in range (10,100):
    if i == 25:
        break
    elif i % 2 == 0:
        print(i, "Bukan prima")
    elif i % 3 == 0:
        print(i, "Bukan prima")
    elif i % 5 == 0:
        print(i, "Bukan prima")
    elif i % 7 == 0:
        print(i, "Bukan prima")
    else:
        print(i, "adalah Bilangan prima")
print("------------------------------------")
