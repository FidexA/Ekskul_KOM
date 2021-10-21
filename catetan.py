# PENJELASAN   |String -> Bisa berisi apa aja, kata, kalimat. |Integer -> Angka. |Boolean -> True/False. |Float -> Angka, but bisa dalam desimal. |Type Casting -> Gabungin
# Variable

namaPanggilan = "Fide" # string
umur = 15 # Integer
laki = True # Boolean
perempuan = False # Boolean
tinggi = 169.69 # Float
namaLengkap = ["Muhammad", "Rafi", "Ghalib", "Fideligo"]

Kalimat = "Nama saya " + namaPanggilan + ". Aku " + str(umur) + " tahun." # type casting

hasil = umur * 10


if perempuan:
    print("saya perempuan")
    
else:
    print("Saya laki-laki")

panjangNama = len(namaLengkap)
print(panjangNama) #4 Harusnya
print(namaLengkap) #Line 9

namaLengkap.append('Bisa Dipanggil Fide') #Menambahkan "Bisa Dipanggil Fide" ke namaLengkap(Line 9)
panjangNamaTambahan = len(namaLengkap)
print(panjangNamaTambahan) #5 harusnya
print(namaLengkap) #Line 9 + Line 26

# FUNCTION
# Function Name
# Function Body
# Parameter (N >= 0)
# Return Value (N >= 0)

def tambah(a, b):
    hasil = a + b
    return hasil

c = tambah(5, 4)
print("Hasilnya adalah " + str(c))

# Percabangan

# if
n = -1

if n < 0:
    print("nilai n negatif!")

# else
a = 10
if n > 0:
    print("nilai a positif!")
else:
    print("nilai a negatif!")

# if else if
b = 10
if b != 0:
    print("b bukan 0! nilai b adalah " + str(b))
elif b == 30:
    print("Ya! Nilai b adalah 30!")
else:
    print("Semua tebakan salah! :(")

# Perulangan
# literasi
# for loop

i = 0
for namaPanggilan in namaLengkap:
    # nama = namaLengkap[index]
    # i += --> i = i + 1
    i += 1
    print(str(i) +" == " + namaPanggilan)

loop = [1,2,3,4,5] # array
for i in loop:
    star = "*" * i # memanfaatkan elemen yg ada dalam array
    print(star)