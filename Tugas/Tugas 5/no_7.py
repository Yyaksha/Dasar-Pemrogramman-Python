a = 1
b = 1
temp = 1

for i in range(10):
  a = b
  b = temp
  temp = a + b
  print(a, end=" ")
print()