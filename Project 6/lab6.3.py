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
    if x <= 0.33:
        chain[0] = 1
        init = stateTrans[1]
    elif x<= 0.66 and x>0.33:
        chain[0] = 2
        init = stateTrans[2]
    elif x > 0.66:
        chain[0] = 3
        init = stateTrans[3]
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
init=[0,0.33,0.33,0.33,0]
chain = [0]*15
chain, steps = generateChain(init, stateTrans, chain)
steps.insert(0,0)
graphChains(chain,steps)
