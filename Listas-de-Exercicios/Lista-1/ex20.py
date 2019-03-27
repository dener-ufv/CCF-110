idade = float(input("Idade: "))
if idade < 16:
  print("Não Eleitor")
elif idade <= 18:
  print("Eleitor Facultativo")
elif idade <= 65:
  print("Eleitor Obrigatório")
else:
  print("Eleitor Facultativo")