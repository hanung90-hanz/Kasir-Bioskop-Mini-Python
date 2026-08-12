print("pesan berapa tiket?")
harga_tiket = 50000
tiket = int(input())
print("berapa umur mu?")
age = int(input())

if age >17:
    harga = 50000
    print("tidak dapat potongan harga")
elif age >= 10 and age <= 15:
    harga = 50000 - (50000 * 0.20)
    print("dapat 20% dicount")
else:
    harga = 50000 - (50000 * 0.50)
    print("dapat 50% dicount")
print(f"harga_tiket: RP {int(harga)}")

print("pilih snack")
snack = (["pop corn"], ["tea"], ["cocholate"])
print("1. pop corn")
print("2. tea")
print("3. cocholate")
snack = int(input())

if snack == 1:
    harga_snack = 15000
    name_snack = "pop corn"
elif snack == 2:
    harga_snack = 10000
    name_snack = "tea"
elif snack == 3:
    harga_snack = 13000
    name_snack = "cocholate"
print(f"kamu memilih : {name_snack} harga RP {harga_snack}")

print("berapa yang ingin kamu beli?")

jumlah = int(input())

total_snack = harga_snack * jumlah
print(f"snack : {jumlah} {name_snack} (RP {total_snack})")

if age >=18:
    print("karena umur mu sudah besar jadi boleh menonton film dewasa")
else:
    print("karena umur mu masih terlalu kecil jadi tidak boleh menonton film dewasa")
