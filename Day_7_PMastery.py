#B_R_R
#M_S_A_W

input_for_systems=input("Two numbers comma-separated:  ")

dimension=[int(x) for x in input_for_systems.split(',')]

rowin=dimension[0]
colin=dimension[1]

list=[[0 for column in range(colin)] for rows in range(rowin)]

for row in range(rowin):

	for col in range(colin):
  
		list[row][col]=row*col
    
print(list)
