gajiPokok = float(input("Masukkan gaji pokok anda :"))
uangTransport = float(input("Masukkan uang transport harian :"))
uangMakan = float(input("Masukkan uang makan harian :"))
tunjanganJabatan = float(input("Masukkan gaji Tunjangan jabatan anda :"))
honorLembur = float(input("Masukkan gaji honor lembur anda :"))

elemenGaji = gajiPokok + uangTransport + uangMakan + tunjanganJabatan + honorLembur

print("Total Gaji keseluruhan anda : %.0f"% elemenGaji)