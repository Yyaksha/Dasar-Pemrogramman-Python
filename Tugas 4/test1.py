anggota_tubuh_cacat = input("Apakah anda memmiliki anggota tubuh cacat? ")

jenis_kelamin = input("Masukkan jenis kelamin :")
berat_badan = int(input("Masukkan berat badan :"))
tinggi_badan = int(input("Masukkan tinggi badan :"))
tahun_lahir = int(input("Masukkan tahun lahir :"))
tahun_sekarang = 2024
usia = tahun_sekarang - tahun_lahir
nilai_akademis = int(input("Masukkan nilai akademis :"))
skill = "memanah"


if anggota_tubuh_cacat == "ya":
  print(f"Anda tidak memenuhi kriteria karena memilik anggota tubuh cacat")
else:
  if jenis_kelamin == "perempuan":
    if 45 <= berat_badan <= 50 and tinggi_badan >= 165 and usia <= 20:
      print(f"Anda memenuhi kriteria 1")
    else:
      print(f"Anda tidak memenuhi kriteria")
  elif jenis_kelamin == "laki laki":
    if berat_badan <= 70 and tinggi_badan >= 170 and usia <= 30:
      print(f"Anda memenuhi kriteria 2")
    else:
      print(f"Anda tidak memenuhi kriteria 2")
  else:
    print(f"jenis kelamin tidak valid")

if nilai_akademis >= 90 and usia <= 30:
  print(f"Anda memenuhi kriteria 3")
else:
  print(f"Anda tidak memenuhi kriteria 3")
if skill == "memanah" or skill == "menembak" or skill == "berkuda":
  print(f"anda memenuhi kriteria 4")
else:
  print(f"anda tidak memenuhi kriteria 4")
    
