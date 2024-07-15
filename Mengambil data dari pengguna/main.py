# Mengambil data dari pengguna

### Mengambil data (Defaultnya pasti String) ###
dataStr = input("Masukan Data: ")
print("Data =" ,dataStr, "Tipenya adalah" ,type(dataStr))

### Mengambil data Float ###
dataFloat = float(input("Masukan Data:"))
print("Data =" ,dataFloat, "Tipenya adalah" ,type(dataFloat))

### Mengambil data Integer ###
dataInt = int(input("Masukan data:"))
print("Data =" ,dataInt, "Tipenya adalah" ,type(dataInt))

### Mengambil data Boolean ###
dataBool = bool(int(input("Masukan data:")))
print("Data =" ,dataBool, "Tipenya adalah" ,type(dataBool))

""" Dalam konteks input pengguna:

Ketika pengguna memasukkan sebuah nilai melalui input(), nilai tersebut berupa string. 
Konversi langsung dari string ke boolean dengan bool() tidak memberikan hasil yang diharapkan karena:

### bool("0") akan menghasilkan True (karena string "0" bukan string kosong).
### bool("1") juga akan menghasilkan True.

Oleh karena itu, langkah perantara konversi ke integer diperlukan untuk memastikan bahwa:

### int("0") menghasilkan 0, yang kemudian dikonversi ke False oleh bool().
### int("1") menghasilkan 1, yang kemudian dikonversi ke True oleh bool(). """