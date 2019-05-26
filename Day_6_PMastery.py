 # B_R_R
 # M_S_A_W
 
 # Creating cool calculator logic 
 
c=50
h=40

# use this formula Q=square root of [(28*c*d)/h]
# find d

import math
x=[]
y=[i for i in input('''

        give me numbers:   
        
                ''').split(',')]
for d in y:
   x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))
