input_a = int(input("masukkan nilai A :"))
input_b = int(input("masukkan nilai B :"))
input_c = int(input("masukkan nilai C :"))

if input_b < input_a and input_c < input_a :
    print(f"Bilangan {input_a} lebih besar dari {input_b} dan {input_c}")
elif input_a < input_b and input_c < input_b:
    print(f"Bilangan {input_b} lebih besar dari {input_a} dan {input_c}")
elif input_b < input_c and input_a < input_c:
    print(f"Bilangan {input_c} lebih besar dari {input_b} dan {input_a}")
elif input_a == input_b and input_a and input_b > input_c:
    print(f"Bilangan A: {input_a} sama dengan B :{input_b}, tapi lebih besar dari C: {input_c}")
elif input_b == input_c and input_b and input_c > input_a:
    print(f"Bilangan B: {input_b} sama dengan C: {input_c}, tapi lebih besar dari A: {input_a}")
elif input_c == input_a and input_c and input_a > input_b:
    print(f"Bilangan C: {input_c} sama dengan A: {input_a}, tapi lebih besar dari B: {input_b}")
else:
    print(f"Bilangan {input_a},{input_b} dan {input_c} sama besar")