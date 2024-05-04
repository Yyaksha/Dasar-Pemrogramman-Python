input_a = int(input("masukkan nilai A :"))
input_b = int(input("masukkan nilai B :"))
input_c = int(input("masukkan nilai C :"))

if input_b > input_a and input_c > input_a:
    print(f"Bilangan {input_a} lebih kecil dari {input_b} dan {input_c}")
elif input_a > input_b and input_c > input_b:
    print(f"Bilangan {input_b} lebih kecil dari {input_a} dan {input_c}")
elif input_b > input_c and input_a > input_c:
    print(f"Bilangan {input_c} lebih kecil dari {input_b} dan {input_a}")
else:
    print(f"Bilangan {input_a},{input_b} dan {input_c} sama besar")