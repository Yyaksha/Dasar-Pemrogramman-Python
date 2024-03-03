algoritma = float(input("Masukkan skor Algoritma :"))
perancangan_objek = float(input("Masukkan skor Perancangan Objek :"))
kalkulus = float(input("Masukkan skor Kalkulus :"))
etika_profesi = float(input("Masukkan skor Etika Profesi :"))
databases = float(input("Masukkan skor Databases :"))
english = float(input("Masukkan skor English :"))

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

total_algoritma = nilai_kredit * skorToBobot(algoritma)
total_perancangan_objek = nilai_kredit * skorToBobot(perancangan_objek)
total_kalkulus = nilai_kredit * skorToBobot(kalkulus)
total_etika_profesi = nilai_kredit * skorToBobot(etika_profesi)
total_databases = nilai_kredit * skorToBobot(databases)
total_english = nilai_kredit * skorToBobot(english)

total_bobot = total_algoritma + total_perancangan_objek + total_kalkulus + total_etika_profesi + total_databases + total_english

def countIps(totalSkor, totalKredit):
  total_ipk = totalSkor / totalKredit
  return total_ipk

print("Total nilai IPK anda : %.2f"%  countIps(total_bobot, 18))