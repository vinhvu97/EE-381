#Vinh Vu
# EE 381 Project 2
import random
import numpy as np
import matplotlib as mp
p_0 = 0.6
e_0 = 0.05
e_1 = 0.03
def nSidedDie(p):
    if sum(p) != 1:
        print('Probability values are incorrect!')
    sides = len(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = np.random.rand()
    for k in range(0,sides):
        if r > cp[k] and r<= cp[k+1]:
            sides = k+1
    return sides
S = nSidedDie([p_0,1-p_0])
S = S - 1
print(S)
if (S == 1):
    R = nSidedDie([e_1,1-e_1])
    R = R - 1
    print(R)
elif (S == 0):
    R = nSidedDie([1-e_0,e_0])
    R = R - 1
    print(R)
