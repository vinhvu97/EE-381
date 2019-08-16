# Vinh Vu
# EE 381 Project 2 Problem 4
import numpy as np
p_0 = 0.6
e_0 = 0.05
e_1 = 0.03
fail = 0
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

for k in range(100000):
    D = int()
    one = int()
    zero = int()
    S = nSidedDie([p_0,1-p_0])
    S = S - 1
    for i in range(3):
        if (S == 1):
            R = nSidedDie([e_1,1-e_1])
            R = R - 1
        elif (S == 0):
            R = nSidedDie([1-e_0,e_0])
            R = R - 1
        if (R == 0):
            zero += 1
        elif (R == 1):
            one += 1
    if (one > zero):
        D = 1
    elif (zero > one):
        D = 0
    if (D!=S):
        fail += 1
fail_rate = fail/100000
print("Fail rate:", fail_rate)

