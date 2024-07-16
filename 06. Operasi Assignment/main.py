# === Operasi Assignment === #
print("\n=== Operasi Assignment ===")

a = 5
print("Nilai a =" , a)   

a += 5 # Sama halnya dengan a = a + 5
print("a =+ 5 maka nilai a berubah menjadi" ,a) # Hasilnya 10
a -= 5 # Sama halnya dengan a = a - 5
print("a -= 5 maka nilai a berubah menjadi" ,a) # Hasilnya 5 karena a diatas berubah menjadi 10
a *= 5 # Sama halnya dengan a = a x 5
print("a *= 5 maka nilai a berubah menjadi" ,a) # Hasilnya 25 karena nilai a sudah menjadi 5

# === Modulus (%) === #
print("\n=== Modulus (%) ===")
b = 5
print("Nilai b =" , b)  
b %= 5
print("b %= 1 maka nilai b berubah menjadi" ,b)

# === Floor Division (//) === #
print("\n=== Floor Division (//) ===")
c = 20
print("Nilai c =" , c)  
c //= 7
print("c //= 1 maka nilai b berubah menjadi" ,c)

# === Operasi Bitwise === #
# OR (|) Jika ada yang True, maka hasilnya True #

print("\n=== Operasi Bitwise OR (|) ===")

d = True
d |= False
print("True | False maka" ,d) # True | False => True

d = True
d |= True
print("True | True maka" ,d) # True | True => True

d = False
d |= True
print("False | True maka" ,d) # False | True => True

d = False
d |= False
print("False | False maka" ,d) # False | False => False

# AND (&) Jika ada dua nilai true, maka hasilnya true #

print("\n=== Operasi Bitwise AND (&) ===")

d = True
d &= False
print("True & False maka" ,d) # True & False => False

d = True
d &= True
print("True & True maka" ,d) # True & True => True

d = False
d &= True
print("False & True maka" ,d) # False & True => False

d = False
d &= False
print("False & False maka" ,d) # False & False => False

# AND (&) Hanya jika ada satu True, maka hasilnya True #

print("\n=== Operasi Bitwise XOR (^) ===")

d = True
d ^= False
print("True ^ False maka" ,d) # True ^ False => True

d = True
d ^= True
print("True ^ True maka" ,d) # True ^ True => False

d = False
d ^= True
print("False ^ True maka" ,d) # False ^ True => True

d = False
d ^= False
print("False ^ False maka" ,d) # False ^ False => False