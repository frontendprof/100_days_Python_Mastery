

#B_R_R
#M_S_A_W

# find all numbers divisible by 7 and not multiple of 5 between 2000 and 3200 inclusive
# solution should be comma separated on a sinle dictionary


empty_list=[]

for i in range(2000, 3201):
  if (i%7==0) and (i%5!=0):
    empty_list.append(str(i))


print("\t ".join(empty_list))

