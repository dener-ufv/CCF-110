s = 0
for i in range(30):
  s += (-1)**i * (480 - 5*i) / (10 + i)
print("Soma: ", s)