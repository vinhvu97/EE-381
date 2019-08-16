import numpy as np
import random
import matplotlib.pyplot as plt

def generateChain(init,stateTrans, chain):
    steps = list(range(0,15))
    for step in steps:
        x = np.random.uniform(0,1)
        if x <= init[0]:
            chain[step] = 'R'
            nextState = stateTrans[0]
        if x > init[0] and x <= init[0]+init[1]:
            chain[step] = 'N'
            nextState = stateTrans[1]
        if x > init[0]+init[1]:            
            chain[step] = 'S'
            nextState = stateTrans[2]
        init = nextState
    return chain, steps

def generateChains(init,stateTrans,chainR, chainN, chainS):
    steps = list(range(0,15))
    for step in steps:
        x = np.random.uniform(0,1)
        if x <= init[0]:
            chainR[step] += 1
            nextState = stateTrans[0]
        if x > init[0] and x <= init[0]+init[1]:
            chainN[step] += 1
            nextState = stateTrans[1]
        if x > init[0]+init[1]:            
            chainS[step] += 1
            nextState = stateTrans[2]
        init = nextState
    return chainR, chainN, chainS, steps

def generateChainUsingMatrix(init,stateTrans,chainR, chainN, chainS):
    p = stateTrans
    curr = init
    for x in range(0,15):    
        chainR[x] = curr[0]
        chainN[x] = curr[1]
        chainS[x] = curr[2]
        curr = init@p
        p = p@stateTrans        
    return chainR, chainN, chainS

def graphChain(chain,steps):
    plt.plot(steps,chain,'r--')
    plt.plot(steps,chain,'x')
    plt.title("Simulated Three-state Markov Chain\nSingle Simulation Run")
    plt.ylabel("State of the Markov Chain")
    plt.xlabel("Step Number")
    plt.ylim(-1,5)
    plt.xticks(np.arange(0, 16, 1))
    plt.show()
    
def graphChains10000(chainR,chainN,chainS,steps):
    maxNum = max(max(chainR),max(chainN),max(chainS))
    minNum = min(min(chainR),min(chainN),min(chainS))
    plt.plot(steps,chainR,'b--',label="Rain")
    plt.plot(steps,chainN,'k--',label="Nice")
    plt.plot(steps,chainS,'r--',label="Snow")
    plt.plot(steps,chainR,'x')
    plt.plot(steps,chainN,'x')
    plt.plot(steps,chainS,'x')
    plt.title("Simulated Three-state Markov Chain\n N = 10000 Simulation Runs")
    plt.ylabel("Probability")
    plt.xlabel("Step number")
    axes = plt.gca()
    axes.set_xlim([-1,16])
    axes.set_ylim([minNum-0.1,maxNum + 0.1])
    plt.xticks(np.arange(0, 16, 1.0))
    plt.legend(loc='lower right')
    plt.show()
    
def graphChainsMatrix(chainR,chainN,chainS,steps):
    maxNum = max(max(chainR),max(chainN),max(chainS))
    minNum = min(min(chainR),min(chainN),min(chainS))
    plt.plot(steps,chainR,'b--',label="Rain")
    plt.plot(steps,chainN,'k--',label="Nice")
    plt.plot(steps,chainS,'r--',label="Snow")
    plt.plot(steps,chainR,'x')
    plt.plot(steps,chainN,'x')
    plt.plot(steps,chainS,'x')
    plt.title("Calculated Three-state Markov Chain\nUsing the State Transition Matrix")
    plt.ylabel("Probability")
    plt.xlabel("Step number")
    axes = plt.gca()
    axes.set_xlim([-1,16])
    axes.set_ylim([minNum-0.1,maxNum + 0.1])
    plt.xticks(np.arange(0, 16, 1.0))
    plt.legend(loc='lower right')
    plt.show()


# Given state transition and initial probabilities
stateTrans = np.array([[0.5,0.25,0.25],[0.25,0.125,0.625],[0.33,0.66,0]])
init = np.array([0.25,0,0.75])

# Create empty lists for each weather condition with 0 filled 15 elements
R = [0]*15
N = [0]*15
S = [0]*15
chain = [0]*15
# Generate three-state Markov chain for single run
chains, steps = generateChain(init, stateTrans, chain)
graphChain(chains, steps)
    
# Generate three-state Markov chain for 10,000 runs
experiments = 10000
for x in range(0,experiments):
    chainR, chainN, chainS, steps = generateChains(init, stateTrans,R, N, S)
chainLength = 15
for y in range(0,chainLength):
    chainR[y] = chainR[y]/experiments
    chainN[y] = chainN[y]/experiments
    chainS[y] = chainS[y]/experiments
graphChains10000(chainR, chainN, chainS, steps)
    
# Generate three-state Markov chain using Matrix
chainR, chainN, chainS = generateChainUsingMatrix(init, stateTrans,R, N, S)
graphChainsMatrix(chainR, chainN, chainS, steps)
    
