uangBelanja = float(input("Masukkan uang belanja :"))
totalBelanja = float(input("Masukkan total belanja :"))
diskon = totalBelanja * (10/100)

if totalBelanja > 700000:
    diskon = totalBelanja * (10/100)
else : diskon = 0

print("Diskon anda sebesar %.0f"% diskon)

setelah_diskon = totalBelanja - diskon
uangKembalian = uangBelanja - setelah_diskon

print("Total kembalian adalah %.0f"% uangKembalian)