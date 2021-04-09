#Menghitung nilai rata-rata
n = int(input('Masukkan banyak data :'))
nilai = []
i = 1
for i in range (n):
    angka = float(input('Masukkan data ke-{} :'.format(i+1)))
    nilai.append(float(angka))
    i = i + 1

#Output
ratarata = sum(nilai)/n
print("Rata - rata :", ratarata)

print("=============================================")

#Menghitung nilai rata-rata dengan while
print(">>>>> Menghitung Nilai Rata-rata data <<<<<")
i = 1
n = int(input("Masukan banyak data :"))
list_data = []

print("--------------------------------------------")

while i <= n:
    data = float(input("Masukkan nilai ke-%d :" % i))
    list_data.append(data)
    i += 1

print("---------------------------------------------")

#Output nilai rata-rata
ratarata = sum(list_data)/n
print("Nilai rata-rata data tersebut adalah :", ratarata)