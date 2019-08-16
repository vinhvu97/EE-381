import numpy as np
import random
import matplotlib.pyplot as plt

def generateChainUsingMatrix2(init,stateTrans,chainA, chainB, chainC, chainD, chainE, chainLength):
    p = stateTrans
    curr = init
    for x in range(0,chainLength):    
        chainA[x] = curr[0]
        chainB[x] = curr[1]
        chainC[x] = curr[2]
        chainD[x] = curr[3]
        chainE[x] = curr[4]
        curr = init@p
        p = p@stateTrans   
    return chainA, chainB, chainC, chainD, chainE

def graphChainsMatrix(chainA,chainB,chainC,chainD,chainE, steps, chainLength,vector):
    maxNum = max(max(chainA),max(chainB),max(chainC),max(chainD),max(chainE))
    minNum = min(min(chainA),min(chainB),min(chainC),min(chainD),min(chainE))
    plt.plot(steps,chainA,'k--',label="A")
    plt.plot(steps,chainB,'b--',label="B")
    plt.plot(steps,chainC,'r--',label="C")
    plt.plot(steps,chainD,'y--',label="D")
    plt.plot(steps,chainE,'c--',label="E")

    plt.title("Calculated Five-state Markov Chain\nUsing the initial probability vector v" + str(vector))
    plt.ylabel("Probability")
    plt.xlabel("Step number")
    axes = plt.gca()
    axes.set_xlim([-1,chainLength + 1])
    axes.set_ylim([minNum-0.1,maxNum + 0.1])
    plt.xticks(np.arange(0, 16, 1.0))
    plt.legend(loc='upper center')
    plt.show()

# Generate first experiment with equal initial probability
steps = list(range(0,20))
stateTrans = np.array([[0,1,0,0,0],[0.5,0,0.5,0,0],[0.33,0.33,0,0,0.33],[1,0,0,0,0],[0,0.33,0.33,0.33,0]])
init = np.array([0.2,0.2,0.2,0.2,0.2])
chainLength = 20
A = [0]*chainLength
B = [0]*chainLength
C = [0]*chainLength
D = [0]*chainLength
E = [0]*chainLength 
vector = 1
chainA, chainB, chainC, chainD, chainE = generateChainUsingMatrix2(init, stateTrans,A, B, C, D, E, chainLength)
graphChainsMatrix(chainA, chainB, chainC, chainD, chainE, steps, chainLength,vector)
print("prob of Page A: ",chainA[len(chainA)-1])
print("prob of Page B: ",chainB[len(chainB)-1])
print("prob of Page C: ",chainC[len(chainC)-1])
print("prob of Page D: ",chainD[len(chainD)-1])
print("prob of Page E: ",chainE[len(chainE)-1])

# Generate second experiment with E being initial webpage
vector = 2
init = np.array([0,0,0,0,1])
chainA, chainB, chainC, chainD, chainE = generateChainUsingMatrix2(init, stateTrans,A, B, C, D, E, chainLength)
graphChainsMatrix(chainA, chainB, chainC, chainD, chainE, steps, chainLength,vector)
    
print("prob of Page A: ",chainA[len(chainA)-1])
print("prob of Page B: ",chainB[len(chainB)-1])
print("prob of Page C: ",chainC[len(chainC)-1])
print("prob of Page D: ",chainD[len(chainD)-1])
print("prob of Page E: ",chainE[len(chainE)-1])
