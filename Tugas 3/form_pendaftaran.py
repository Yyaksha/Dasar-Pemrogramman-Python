Nama = input("Masukkan nama :")
tempatLahir = input("Masukkan Tempat Lahir :")
tanggalLahir = float(input("Masukkan Tanggal Lahir :"))
tahunLahir = float(input("Masukkan Tahun Lahir :"))
jenisKelamin = input("Masukkan jenis Jenis Kelamin :")
nilaiPelajaran_inggris = float(input("Masukkan nilai Inggris :"))
nilaiPelajaran_MTK = float(input("Masukkan nilai MTK :"))
nilaiPelajaran_indonesia = float(input("Masukkan nilai Indonesia :"))
rata_rataNIlai = (nilaiPelajaran_inggris + nilaiPelajaran_MTK + nilaiPelajaran_indonesia) / 2
tahunSekarang = 2024
umur = tahunSekarang - tahunLahir

if umur >= 25:
  print("Umur anda melebihi persyaratan")
elif rata_rataNIlai >= 80 and jenisKelamin == "laki laki":
  print(f"Dengan nilai rata-rata :{rata_rataNIlai} dan jenis kelamin {jenisKelamin}, anda disarankan masuk jurusan Teknik Informatika")
elif rata_rataNIlai >= 80 and jenisKelamin == "perempuan":
  print(f"Dengan nilai rata-rata :{rata_rataNIlai} dan jenis kelamin {jenisKelamin}, anda disarankan masuk jurusan Sistem Informasi")
else:
  print(f"Dengan nilai rata-rata :{rata_rataNIlai} Anda disarankan masuk jurusan DKV")