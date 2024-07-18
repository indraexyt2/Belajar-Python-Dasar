# === Format string width dan aligment === #

# Data

nama = "Indra"
umur = 24
tinggi_badan = 189

# string standard
print("\n"+ 5*"=" + " String Standart " + 5*"=")
Data = f"Nama : {nama}, Umur : {umur}, Tinggi Badan : {tinggi_badan}"
print(Data)

# String Multiline (\n = Enter)
print("\n"+ 5*"=" + " String Multiline " + 5*"=")
Data = f"Nama : {nama}, \nUmur : {umur}, \nTinggi Badan : {tinggi_badan}"
print(Data)

# String Multiline ("""  """)
print("\n"+ 5*"=" + " String Multiline 3 Kutip " + 5*"=")
Data = f"""Nama : {nama} 
Umur : {umur} 
Tinggi Badan : {tinggi_badan}"""
print(Data)

# Mengatur lebar
print("\n"+ 5*"=" + " Mengatur Lebar " + 5*"=")
Data = f"""
Nama            : {nama:<10} 
Umur            : {umur:<10} 
Tinggi Badan    : {tinggi_badan:<10}"""
print(Data)

