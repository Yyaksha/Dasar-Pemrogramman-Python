name = "SUKABUMII"
x = len(name)

for i in range(5,0,-1):
  for j in range(len(name)):
    if (j>=i-1) and (j<10-i):
      print(name[j], end=" ")
    else:
      print("*", end=" ")
  print()

# name = "SUKABUMII"

# for i in range(5):
#   for j in range(len(name)):

#     if (j>=i) and (j<9-i):
#       print(name[j], end=" ")
#     else:
#       print("*", end=" ")
#   print()

# * * * * B * * * *
# * * * A B U * * *
# * * K A B U M * *
# * U K A B U M I *
# S U K A B U M I I