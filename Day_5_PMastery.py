# B_R_R
# M_S_A_W

# Create a clasa that has two methods
# 1. getString method grabs stings from input
# 2. printString method prints out the getString value

class Mama(object):
  def __init__(self):
    self.s=""
  def getString(self):
    self.s=input("Give me your string to be capitalized: \n")
  def printString(self):
    print(self.s.upper())


x=Mama()
print(x)

# calling a class print out Mama memory location
# if you want actually execute a class you have to call it

x.getString()
x.printString()
