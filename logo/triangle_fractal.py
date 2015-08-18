from tealight.logo import move, turn

def tri(scale):
  for i in range(3):
    move(scale)
    turn(180 - 60)
    
tri(12)