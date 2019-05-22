# B_R_R
# M_S_A_W

# given integral number n, create a dictionary with functions key and value in which value is equal to square of that key.

num = int(input("Enter a number: "))

d=dict()

for i in range(1, num+1):
  d[i]=i*i

print(d)
