import numpy as np

alist = [1,2,3,4]

blist = [5,6,7,8]

a = np.array(alist)
b = np.array(blist)

z = a @ b

print(z)