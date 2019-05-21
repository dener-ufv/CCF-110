tests = 0
soma  = 0
while True:
  read = input().split(' ')
  w1 = int(read[0])
  w2 = int(read[1])
  r  = int(read[2])
  if(w1 == 0 and w2 == 0 and r == 0):
    break
  m = (w1 + w2)*(30 + r)/60
  if(m >= 1 and m < 13):
    print("Nao vai da nao")
  elif m < 14:
    print("E 13")
  elif m < 40:
    print("Bora, hora do show! BIIR!")
  elif m <= 60:
    print("Ta saindo da jaula o monstro!")
  elif m > 60:
    print("AQUI E BODYBUILDER!!")  
  
  tests += 1
  soma += m

media = soma / tests
if media > 40:
  print("\nAqui nois constroi fibra rapaz! Nao e agua com musculo!")
