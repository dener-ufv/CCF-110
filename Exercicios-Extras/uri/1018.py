value = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(value)
for nota in notas:
  print("{0} nota(s) de R$ {1},00".format(value//nota, nota))
  value %= nota