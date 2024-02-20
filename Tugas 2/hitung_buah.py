jerukDibeli = float(input("Masukkan berapa kilo jeruk :"))
apelDibeli = float(input("Masukkan berapa kilo apel :"))
manggaDibeli = float(input("Masukkan berapa kilo mangga :"))
manggisDibeli = float(input("Masukkan berapa kilo manggis :"))
durianDibeli = float(input("Masukkan berapa kilo durian:"))

jeruk = 15000
apel = 30000
mangga = 20000
manggis = 7000
durian = 50000

jumlahHarga = (jerukDibeli * jeruk) + (apelDibeli * apel) + (manggaDibeli* mangga) + (manggisDibeli * manggis) + (durianDibeli * durian)
print("Jumlah Total harga : %.0f"% jumlahHarga)