input_a = int(input("masukkan bilangan A :"))
input_b = int(input("masukkan bilangan B :"))

if input_a > input_b:
    print(f"input {input_a} lebih besar dari {input_b}")
elif input_b > input_a:
    print(f"input {input_b} lebih besar dari {input_a}")
else:
    print(f"input {input_a} sama besar dengan input {input_b}")