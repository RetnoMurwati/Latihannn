for i in range (1, 11):
        for j in range(1, i+1):
            print('%d ' % (i*j), end='')
        print()


for i in range (1, 11):
        for j in range(1, 11):
            print(i*j, end='\t')
            if j == 5:
                break
        print()