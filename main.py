# ==== For Loop === #

# List
print("\n",5*"=", " List ", 5*"=")
buah = ["apel", "pisang", "ceri", "mangga", "jeruk"]
for b in buah:
    panjang = len(b)
    print(f"Nama buah: {b}, Panjang karakter: {panjang}")

# Range
print("\n",5*"=", " Range ", 5*"=")
for i in range(1, 11):
    if i % 2 != 0:
        print(f"Bilangan ganjil: {i}")

# String
print("\n",5*"=", " String ", 5*"=")
kalimat = "halo, saya Indrawansyah"
vokal = "aiueo"
jumlah_vokal = 0

for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")

##
for nama in kalimat:
    print(nama)

# Range
print("\n",5*"=", " Range ", 5*"=")
# Membuat tabel perkalian 1 sampai 5
for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(f"{i} x {j} = {hasil}", end="\t")
    print()  # Ganti baris setelah setiap baris perkalian
