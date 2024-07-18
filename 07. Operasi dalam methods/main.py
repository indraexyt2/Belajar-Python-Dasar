# === Operasi dalam Methods === #
 
# Merubah ke huruf besar semua (Upper)

print("\n=== Upper Case ===")
a = "indrawansyah ganteng"
print("Data awal =" ,a)
print("Ubah ke upper =" ,a.upper())
	

# Merubah ke huruf kecil semua (Lower)

print("\n=== Upper Case ===")
a = "INDRAWANSYAH GANTENG"
print("Data awal =" ,a)
print("Ubah ke lower =" ,a.lower())

# Method is

print("\n=== Method IS ===")
a = "INDRA"
IsUpper = a.isupper()
IsLower = a.islower()
print("Apakah" ,a, "adalah Upper" ,IsUpper)
print("Apakah" ,a, "adalah Upper" ,IsLower)

# islower() <- untuk pengecekan apakah lower case semua
# isalpha() <- untuk mengecek apakah huruf semua
# isalnum() <- apakah huruf dan angka
# isdecimal() <- apakah numeric
# isspace() <- apakah isinya spasi, tab dan enter (newline \n)
# istitle() <- huruf pertama setiap kata upper case

# startwith() dan endwith()

print("\n=== Starwith dan Endwith ===")
a = ("indrawansyah Keren")
print("Apakah nilai a diawali dengan indra = ", a.startswith("indra"))
print("Apakah nilai a diakhiri dengan Keren =", a.endswith("Keren"))

# Catatan => Harus perhatikan besar kecilnya

# Join dan Split

print("\n=== Join dan Split ===")
a = ['Indra', 'Wansyah', 'Keren']
GabungA = " ".join(a) # join spasi
print(GabungA)
print(GabungA.split())

print("\n")
a = "Indra@@Wansyah@@Keren@@Banget"
Pisah = a.split("@@")
print("Split @@ menjadi" ,Pisah)
print("Join hasil Split menjadi", ' '.join(Pisah))
