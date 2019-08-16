import numpy as np
import matplotlib
import matplotlib.pyplot as plt

p = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
N = 10000
n = 1000
X = []
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

for i in range(N):
    success = 0
    for j in range(n):
        Roll_1 = nSidedDie(p)
        Roll_2 = nSidedDie(p)
        Roll_3 = nSidedDie(p)
        if (Roll_1 == 1) and (Roll_2 == 2) and (Roll_3 == 3):
            success += 1
    X.append(success)
    
b=range(1,18)
sb=len(b)
h1, bin_edges = np.histogram(X,bins=b)
b1=bin_edges[0:sb-1]

fig2=plt.figure(2)
p1=h1/N
plt.stem(b1,p1)
plt.title('Bernoulli Trials: PMF - Experiment Results')
plt.xlabel('Number of Successes in n=1000 trials')
plt.ylabel('Probability')
plt.xticks(b1)
plt.show()
