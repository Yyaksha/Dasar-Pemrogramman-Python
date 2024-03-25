#1
a = "Aku cinta indonesia"
r = 1

for i in range(3):
  print(f"{r}. {a}")
  r += 2

#2
c = 2
d = 2

for i in range(6):
  print(c, end=" ")
  c += d
  d += 1

#3
e = 1
f = 1

for i in range(3):
  result = e * f
  print(f"{e} x {f} = {result}")
  f += 1

#4
g = 7
h = 6

for i in range(5):
  result2 = g * h
  print(f"{g} x {h} = {result2}")
  h += 1

#5
j = ". "
k = "*"

for i in range(3):
  j += k
  k = 3
  print(j)