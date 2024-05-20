no = [1,2,3,2,4,3,5]
no2 = []

for i in no:
  if i != 2:
    no2.append(i)
no2.sort()
no2.reverse()

print(no2)