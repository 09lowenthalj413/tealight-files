from tealight.art import *

c = [(100,100), (5,50), (200,300), (260, 50), (370, 400), (290,20), (280,50),(275,10)]
fill_polygon(c)

color("red")
#line(50,60,1000,60)
#spot(287.89,60,5)

density = 5

for i in range(0,500,density):
  for j in range(0,500,density):  
    if test_polygon(i,j,c):
      color("rgba(255,0,0,0.5)")
    else:
      color("blue")
    spot(i,j,2)    

if __name__ == "__main__":
  print "Test: " + str(test_polygon(50,50,c))

  