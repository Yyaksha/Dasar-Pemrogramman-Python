huruf = ['O', 'S' ]

for i in range(5,0,-1):
  for j in range(i):
    print(huruf[(i + j) % 2], end=" ")
  print()