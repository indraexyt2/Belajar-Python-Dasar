# Aritmatika

a = 10
b = 5

# Pertambahan +
hasil = a + b
print(a,'+',b,'=',hasil)

# Pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# Perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# Eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# Modulus % --- Sisa pembagian, mis. 10 mod 3 = 1
hasil = a % b
print(a,'%',b,'=',hasil)

# Floor division // Pembagian yang dibulatkan
hasil = a // b
print(a,'//',b,'=',hasil)

# Meminta data pada user dan melakukan operasi artimatika

# Penjumlahan 2 angka
Data1 = int(input("Masukan data: "))
Data2 = int(input("Masukan data: "))
hasil = Data1 + Data2
print("Hasilnya adalah "  + str(hasil))

# Pengurangan 2 angka
Data1 = int(input("Masukan data: "))
Data2 = int(input("Masukan data: "))
hasil = Data1 - Data2
print("Hasilnya adalah "  + str(hasil))

# Pembagian 2 angka
Data1 = int(input("Masukan data: "))
Data2 = int(input("Masukan data: "))
hasil = Data1 / Data2
print("Hasilnya adalah "  + str(hasil))

# Eksponen
Data1 = int(input("Masukan data: "))
Data2 = int(input("Masukan data: "))
hasil = Data1 ** Data2
print("Hasilnya adalah "  + str(hasil))

# ==== Catatan ==== #
# Tanda kurung akan membuat hasil dihitung duluan

Data1 = int(input("Masukan data: "))
Data2 = int(input("Masukan data: "))
Data3 = int(input("Masukan data: "))
hasil = Data1 * Data2 * (Data3 + Data1)
print("Hasilnya adalah "  + str(hasil))
