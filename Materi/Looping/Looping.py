name = "YAKSHAA"
x = 5

for i in range(len(name)):
  for j in range(len(name)):
    if (j>i-1):
      print(name[j], end=" ")
    else:
      print("*", end=" ")
  print()