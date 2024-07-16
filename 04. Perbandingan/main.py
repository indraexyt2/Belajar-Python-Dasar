# Operator Perbandingan >,<,>=,<=
a = 10
b = 20

print("a =", a)
print("b =", b)

# Lebih besar dari
print("a > b:", a > b)  # False

# Lebih kecil dari
print("a < b:", a < b)  # True

# Lebih besar atau sama dengan
print("a >= b:", a >= b)  # False

# Lebih kecil atau sama dengan
print("a <= b:", a <= b)  # True

# Sama dengan
print("a == b:", a == b)  # False

# Tidak sama dengan
print("a != b:", a != b)  # True

# Operator Identitas is, is not, ==
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("\nx =", x)
print("y =", y)
print("z =", z)

# Menggunakan is
print("x is y:", x is y)  # False, karena x dan y adalah objek yang berbeda meskipun nilainya sama
print("x is z:", x is z)  # True, karena z merujuk ke objek yang sama dengan x

# Menggunakan is not
print("x is not y:", x is not y)  # True, karena x dan y adalah objek yang berbeda
print("x is not z:", x is not z)  # False, karena z merujuk ke objek yang sama dengan x

# Menggunakan ==
print("x == y:", x == y)  # True, karena nilai x dan y sama
print("x == z:", x == z)  # True, karena z merujuk ke objek yang sama dengan x

### Catatan ###

# Membandingkan small integers (cache Python untuk small integers)
x = 10
y = 10

print("x is y:", x is y)  # True, karena small integers di-cache dan merujuk ke objek yang sama
print("x == y:", x == y)  # True, karena nilai x dan y sama
