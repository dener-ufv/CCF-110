bits = input()
count1 = 0
for bit in bits:
  if bit == '1':
    count1 += 1
if count1 % 2 == 0:
  print(bits+'0')
else:
  print(bits+'1')