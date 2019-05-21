# Clockwise: True
# Anticlockwise: False
clockwise = True

# Start on top: True
# Start on bottom: False
sTop = True

# Start on left side: True
# Start on right side: False
sLeft = False

# size: y * x (rows * columns)
y = 3
x = 5

# matrix
matrix = [[0 for j in range(x)] for i in range(y)]

# sys: directions
RIGHT  = 0
LEFT   = 1
TOP    = 2
BOTTOM = 3

# sys: order to follow
# sys: incr is the increment of step
if clockwise:
  order = [RIGHT, BOTTOM, LEFT, TOP]
else:
  order = [BOTTOM, LEFT, TOP, RIGHT]

# sys: step (represents the step in the order)
# sys: EX. step=2 in clockwise order is LEFT
# sys: EX. step=0 in anticlockwise order is BOTTOM
# sys: Indexes (i, j)
if sLeft and sTop:
  step = 0
  i, j = 0, 0
if not sLeft and sTop:
  step = 1
  i, j = 0, x-1
if not sLeft and not sTop:
  step = 2
  i, j = y-1, x-1
if sLeft and not sTop:
  step = 3
  i, j = y-1, 0

# sys: limits (inclusive)
limL = 0
limR = x-1
limT = 0
limB = y-1

# inicial value 
value = 1

# sys: loop to insert values
for v in range(x*y):
  
  # sys: inser value
  matrix[i][j] = value
  
  # update value to whatever you want
  value += 1

  # sys: the next 51 lines are used to verify if the index is in the limit and update i and j
  if order[step] == RIGHT:
    if j == limR:
      if clockwise: 
        step = (step + 1) % 4
        i += 1
        limT += 1
      else:
        step = (step - 1) % 4
        i -= 1
        limB -= 1
    else:
      j += 1
  
  elif order[step] == LEFT:
    if j == limL:
      if clockwise: 
        step = (step + 1) % 4
        i -= 1
        limB -= 1
      else:
        step = (step - 1) % 4
        i += 1
        limT += 1
    else:
      j -= 1
  
  elif order[step] == TOP:
    if i == limT:
      if clockwise: 
        step = (step + 1) % 4
        j += 1
        limL += 1
      else:
        step = (step - 1) % 4
        j -= 1
        limR -= 1
    else:
      i -= 1
  
  elif order[step] == BOTTOM:
    if i == limB:
      if clockwise: 
        step = (step + 1) % 4
        j -= 1
        limR -= 1
      else:
        step = (step - 1) % 4
        j += 1
        limL += 1
    else:
      i += 1


# print matrix
for line in matrix:
  print(line)