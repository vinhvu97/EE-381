import numpy as np
import random as rand
import matplotlib
import matplotlib.pyplot as plt
import math

def generatePopulation():
    N = 1500000
    mean = 55
    sigma = 5
    randomVariable =list(np.random.randn(N)*sigma + mean)
    return randomVariable

def effectSampleSize():
    population = generatePopulation()
    mean = 55
    sigma = 5
    sampleMean = []
    sampleSigmaPos95 = []
    sampleSigmaNeg95 = []
    sampleSigmaPos99 = []
    sampleSigmaNeg99 = []
    n = list(range(1,201))
    for size in n:
        sample = list(rand.sample(population,size))
        sMean = sum(sample)/size
        sampleMean.append(sMean)
        sSigma = sigma/math.sqrt(size)
        sampleSigmaPos95.append(mean+(1.96*sSigma))
        sampleSigmaNeg95.append(mean-(1.96*sSigma))
        sampleSigmaPos99.append(mean+(2.58*sSigma))
        sampleSigmaNeg99.append(mean-(2.58*sSigma))
    
    plt.plot(n,sampleMean,'x')
    plt.plot(n,sampleSigmaPos95,'r--')
    plt.plot(n,sampleSigmaNeg95,'r--')
    #plt.axhline(y=75)
    plt.title("Sample Means and 95% confidence intervals")
    plt.ylabel("x_bar")
    plt.xlabel("Sample size")
    plt.show()

    plt.plot(n,sampleMean,'x')
    plt.plot(n,sampleSigmaPos99,'g--')
    plt.plot(n,sampleSigmaNeg99,'g--')
    #plt.axhline(y=75)
    plt.title("Sample Means and 99% confidence intervals")
    plt.ylabel("x_bar")
    plt.xlabel("Sample size")
    plt.show()
effectSampleSize()
