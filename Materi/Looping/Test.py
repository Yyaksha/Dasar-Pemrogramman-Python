# name = "000000000000"

# for i in range(9):
#   for j in range(len(name)):
#     if (j>=3-i) and (j<=i+8) and (i<4+j) and (j<4+i) and (j==5-i):
#       print(name[j], end=" ")
#     else:
#       print("*", end=" ")
#   print()

n = 3

if n % 2 == 0 and n >= 2 and n <=5:
    print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
else:
    print("Weird")
