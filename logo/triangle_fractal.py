from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(120)
    

for i in range(-10, 0):
  tri(2**(-i))