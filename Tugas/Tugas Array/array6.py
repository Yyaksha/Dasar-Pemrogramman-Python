no = [8,3,12,4,7,2]
no2 = []

for i in no:
  if i < 5:
    no2.append(0)
  else:
    no2.append(i)
no2.sort()
no2.reverse()

print(no2)