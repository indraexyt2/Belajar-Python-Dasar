# ===== Operasi Logika Boolean ==== #
A = True
B = False

# === OR === #
# Jika ada yang True, maka hasilnya True #

print("\n=== OR ===")

print("True OR True maka hasilnya: " ,A or A) # ==> True
print("True OR False maka hasilnya: " ,A or B) # ==> True
print("False OR False maka hasilnya: " ,B or B) # ==> False
print("False OR True maka hasilnya: " ,B or A) # ==> True
 
# === AND === #
# Jika ada dua nilai true, maka hasilnya true #

print("\n=== AND ===")

print("True AND True maka hasilnya: " ,A and A) # ==> True
print("True AND False maka hasilnya: " ,A and B) # ==> False
print("False AND False maka hasilnya: " ,B and B) # ==> False
print("False AND True maka hasilnya: " ,B and A) # ==> False

# === XOR === #
# Hanya jika ada satu True, maka hasilnya True #

print("\n=== XOR ===")


print("True XOR True maka hasilnya: " ,A ^ A) # ==> False
print("True XOR False maka hasilnya: " ,A ^ B) # ==> True
print("False XOR False maka hasilnya: " ,B ^ B) # ==> False
print("False XOR True maka hasilnya: " ,B ^ A) # ==> True
