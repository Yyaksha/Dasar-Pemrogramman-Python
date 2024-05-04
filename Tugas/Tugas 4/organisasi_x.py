anggota_tubuh_cacat = input("Apakah anda memmiliki anggota tubuh cacat? ")
jenis_kelamin = input("Masukkan jenis kelamin :")
berat_badan = int(input("Masukkan berat badan :"))
tinggi_badan = int(input("Masukkan tinggi badan :"))
tahun_lahir = int(input("Masukkan tahun lahir :"))
tahun_sekarang = 2024
usia = tahun_sekarang - tahun_lahir
nilai_akademis = int(input("Masukkan nilai akademis :"))
skill = input("Masukkan Skill :")

if anggota_tubuh_cacat == "ya":
  print(f"Anda tidak memenuhi kriteria karena memilik anggota tubuh cacat")
elif jenis_kelamin == "perempuan" and berat_badan >= 45 and berat_badan <= 50 and tinggi_badan >= 165 and usia <= 20:
    print(f"Anda memenuhi kriteria 1")
elif jenis_kelamin == "laki laki" and berat_badan <= 70 and tinggi_badan >= 170 and usia <= 30:
    print(f"Anda memenuhi kriteria 2")
elif jenis_kelamin == "laki laki" or jenis_kelamin == "perempuan" and nilai_akademis >= 90 and usia <= 30:
    print(f"Anda memnuhi kriteria 3")
elif jenis_kelamin == "laki laki" or jenis_kelamin == "perempuan" and skill == "menembak" or skill == "memanah" or skill == "berkuda":
    print(f"Anda memenuhi kriteria 4")
else:
  print(f"Anda tidak lolos karena tidak memenuhi kriteria")