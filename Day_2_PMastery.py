# B_R_R
# M_S_A_W

# Compute the factorial of a given number
# Factorial is the integer product of a number and all the numbers below it

def factorial():
  fact=1

  num=int(input("what is your number?  "))
  for i in range(num, 1, -1):
    fact=fact*i
  return fact

print(factorial())
