import numpy as np

arr=np.arange(1,101)
squared=[]

for i in arr:
    squared.append(i**2)

squared =np.array(squared)
print ("squared numbers:", squared ) 