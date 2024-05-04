#Diketahui Harga laptop Zaid Abdullah adalah 39.000.000, dengan masa manfaat 7 tahun dan nilai sisa setelah 7 tahun di perkirakan sebesar 4.000.000. Berapakah Nilai Aset Laptop Bapak Zaid Abdullah setelah 3 tahun?

harga_laptop = int(input("Masukkan harga laptop :"))
masa_manfaat = int(input("Masukkan Masa manfaat :"))
masa_pakai = int(input("Masukkan Masa pakai :"))

SusutTahunan = (harga_laptop - masa_manfaat)/ masa_pakai
harga_laptop_sudah_menyusut = SusutTahunan * 3
Nilai_Aset_Tersisa = harga_laptop - harga_laptop_sudah_menyusut

print(f"Nilai Aset Laptop Bapak Zaid adalah : {Nilai_Aset_Tersisa}")