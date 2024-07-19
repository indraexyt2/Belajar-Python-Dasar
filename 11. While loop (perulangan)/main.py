# ==== While Loop === #

# Menghitung 1-5
i = 1
while i <= 5:
    print(i)
    i += 1

# Menghitung jumlah angka ganjil
i = 1
jumlah_ganjil = 0
while i <= 10:
    if i % 2 != 0:
        jumlah_ganjil += 1
    i += 1
print(f"Jumlah angka ganjil dari 1 hingga 10 adalah: {jumlah_ganjil}")

# Mengiterasi list
buah = ["apel", "pisang", "ceri"]
i = 0
while i < len(buah):
    print(buah[i])
    i += 1

# 
while True:
    inp = input("Masukkan sesuatu (ketik 'keluar' untuk berhenti): ")
    if inp == "keluar":
        print("Berhenti.")
        break
    print(f"Kamu memasukkan: {inp}")


