# retorna Verdadeiro se existe uma posição livre a direita
def hasRight(mat, size, pos_i, pos_j):
  if pos_j == size-1:
    return False
  else:
    return mat[pos_i][pos_j + 1] == -1

# retorna Verdadeiro se existe uma posição livre abaixo
def hasBottom(mat, size, pos_i, pos_j):
  if pos_i == size-1:
    return False
  else: 
    return mat[pos_i + 1][pos_j] == -1

# retorna Verdadeiro se existe uma posição livre a esquerda
def hasLeft(mat, pos_i, pos_j):
  if pos_j == 0:
    return False
  else:
    return mat[pos_i][pos_j - 1] == -1

# retorna Verdadeiro se existe uma posição livre a cima
def hasTop(mat, pos_i, pos_j):
  if pos_i == 0:
    return False
  else:
    return mat[pos_i - 1][pos_j] == -1

# cria uma matriz com todos os campos com o valor -1 (isso vai auxiliar na busca)
def generate(n, m): 
  matrix = []
  while len(matrix) != n:
    matrix.append([])
  for i in range(n):
    while len(matrix[i]) != m:
      matrix[i].append(-1)  
  return matrix

# função resposavel por exibir a matriz na tela
def show(mat):
  size = len(mat)
  for i in range(size):
    print(mat[i])


# pede ao usuário que digite os valores
print("Este programa insere números em uma matrix(NxM) de forma expiral, começando por 1 e terminando em N vezes M")
size_n = int(input("digite o tamanho da matrix(N): "))
size_m = int(input("digite o tamanho da matriz(M): "))
print("")

# cria a matriz com os valores fornecidos pelo usuario
mat = generate(size_n, size_m)

# vvariaveis de controle
### end: é Verdadeiro se todos os valores foram devidamente inseridos
end = False
### i and j: representa a posição do "cursor"
i = 0
j = 0
### counter: valor que vai ser inserido na matriz
counter = 0
### opçõe de movimento: 0-direita 1-baixo 2-esquerda 3-cima
move = 0 

while not end:
  mat[i][j] = counter + 1
  end = counter == size_n*size_m - 1
  
  if move == 0:
    if hasRight(mat, size_m, i, j):
      j += 1
      counter += 1
    else:
      move = 1

  if move == 1:
    if hasBottom(mat, size_n, i, j):
      i += 1
      counter += 1
    else:
      move = 2

  if move == 2:
    if hasLeft(mat, i, j):
      j -= 1
      counter += 1
    else:
      move = 3
  
  if move == 3:
    if hasTop(mat, i, j):
      i -= 1
      counter += 1
    else:
      move = 0
  
show(mat)
