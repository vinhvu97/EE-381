import numpy as np
import random
import matplotlib.pyplot as plt

def compareLists(listA,listB):
    for i in range(len(listA)):
        if listA[i] != listB[i]:
            return False
    return True

def generateChain(init,stateTrans, chain):
    steps = list(range(1,15))
    x = np.random.uniform(0,1)
    chain[0] = 2
    init = stateTrans[2]
    for step in steps:
        x = np.random.uniform(0,1)
        if (compareLists(init,stateTrans[0])):
            chain[step] = 0
            if x <= 1:
                nextState = stateTrans[0]
                
        if (compareLists(init,stateTrans[1])):
            chain[step] = 1
            if x <= 0.3:
                nextState = stateTrans[0]
            else:
                nextState = stateTrans[2]
                
        if (compareLists(init,stateTrans[2])):
            chain[step] = 2
            if x <= 0.5:
                nextState = stateTrans[1]
            else:
                nextState = stateTrans[3]
                
        if (compareLists(init,stateTrans[3])):
            chain[step]=3
            if x <= 0.6:
                nextState = stateTrans[2]
            else:
                nextState = stateTrans[4]

        if (compareLists(init,stateTrans[4])):
            chain[step] = 4
            if x <= 1:
                nextState = stateTrans[4]
        init = nextState
    return chain, steps
def graphChains(chain,steps):
    plt.plot(steps,chain,'r:')
    plt.plot(steps,chain,'x')
    plt.title("A Sample of Drunkard's Walk")
    plt.ylabel("State")
    plt.xlabel("Step Number")
    plt.ylim(-1,5)
    plt.xticks(np.arange(0, 16, 1))
    plt.show()
stateTrans = np.array([[1,0,0,0,0],[0.3,0,0.7,0,0],[0,0.5,0,0.5,0],[0,0,0.6,0,0.4],[0,0,0,0,1]])
init=[0,0,1,0,0]
absorb_4 = 0
absorb_0 = 0
for i in range(10000):
    chain = [0]*15
    chain, steps = generateChain(init, stateTrans, chain)
    steps.insert(0,0)
    if chain[14] == 4:
        absorb_4+=1
    if chain[14] == 0:
        absorb_0+=1
chance_0 = absorb_0/10000
chance_4 = absorb_4/10000
print("Absorbtion Probabilities for state 0:",chance_0)
print("Absorbtion Probabilities for state 4:",chance_4)

