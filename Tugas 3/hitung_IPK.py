mtk_diskrit = float(input("Masukkan skor mtk diskrit :"))
aljabar_linier = float(input("Masukkan skor aljabar linier :"))
basis_data = float(input("Masukkan skor basis data :"))
dasar_pemrogramman = float(input("Masukkan skor dasar pemrogramman :"))
sistem_operasi = float(input("Masukkan skor sistem operasi :"))
pkn = float(input("Masukkan skor pkn :"))
inggris = float(input("Masukkan skor inggris :"))

def skorToBobot(skor):
  if skor >= 90:
    return 4
  elif skor >= 85:
    return 3.75
  elif skor >= 80:
    return 3.5
  elif skor >= 75:
    return 3.25
  elif skor >= 70:
    return 3
  elif skor >= 65:
    return 2.75
  elif skor >= 60:
    return 2.5
  elif skor >= 55:
    return 2.25
  else:
    return 2.0
  
nilai_kredit = 3

total_mtk_diskrit = nilai_kredit * skorToBobot(mtk_diskrit)
total_aljabar_linier = nilai_kredit * skorToBobot(aljabar_linier)
total_basis_data = nilai_kredit * skorToBobot(basis_data)
total_dasar_pemrogramman = nilai_kredit * skorToBobot(dasar_pemrogramman)
total_sistem_operasi = nilai_kredit * skorToBobot(sistem_operasi)
total_pkn = nilai_kredit * skorToBobot(pkn)
total_inggris = nilai_kredit * skorToBobot(inggris)

total_bobot = total_mtk_diskrit + total_aljabar_linier + total_basis_data + total_dasar_pemrogramman + total_sistem_operasi + total_pkn + total_inggris

def countIps(totalSkor, totalKredit):
  total_ipk = totalSkor / totalKredit
  return total_ipk

print("Total nilai IPK anda :" , countIps(total_bobot, 21))