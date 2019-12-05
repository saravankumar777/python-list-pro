###cartesian product of two lists###
from itertools import product
a=[1,2,3,4,];
b=[6,7,8,9,];
c=list(product(a,b))
print("the cartesian product of a and b is:",c)
