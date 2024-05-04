huruf = ['A', 'B']
for i in range(5):
  for j in range(5):
    print(huruf[(i + j) % 2], end=" ")
  print()