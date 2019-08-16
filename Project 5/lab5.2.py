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
def estimatingPopulationMean(sampleSize):
    M = 10000
    mean = 55
    sigma = 5
    success95normal = 0
    success99normal = 0
    success95t = 0
    success99t = 0
    population = generatePopulation()
    count = 0
    v = sampleSize - 1
    while count < M:
        sample = list(rand.sample(population,sampleSize))
        sampleMean = sum(sample) / sampleSize
        sHatCalc = [(x - sampleMean)**2 for x in sample]
        sHat = math.sqrt(sum(sHatCalc)/(sampleSize-1))

        normal95StandardError = 1.96*(sHat / math.sqrt(sampleSize))
        normal95Interval = [sampleMean - normal95StandardError, sampleMean + normal95StandardError]
        if mean >= normal95Interval[0] and mean <= normal95Interval[1]:
            success95normal += 1

        normal99StandardError = 2.576 * (sHat / math.sqrt(sampleSize))
        normal99Interval = [sampleMean - normal99StandardError, sampleMean + normal99StandardError]
        if mean >= normal99Interval[0] and mean <= normal99Interval[1]:
            success99normal += 1
        if v == 4:
            t95 = 2.78
            t99 = 4.6
        if v == 39:
            t95 = 2.02
            t99 = 2.7
        if v == 119:
            t95 = 1.98
            t99 = 2.62
        t95StandardError = t95 * (sHat / math.sqrt(sampleSize))
        t95Interval = [sampleMean -t95StandardError, sampleMean + t95StandardError]
        if mean >= t95Interval[0] and mean <= t95Interval[1]:
            success95t += 1
            
        t99StandardError = t99*(sHat / math.sqrt(sampleSize))
        t99Interval = [sampleMean-t99StandardError, sampleMean + t99StandardError]
        if mean >= t99Interval[0] and mean <= t99Interval[1]:
            success99t += 1
        count += 1
    
    
    percentSuccess95Normal = success95normal / M
    percentSuccess99Normal = success99normal / M
    percentSuccess95t = success95t / M
    percentSuccess99t = success99t / M

    print("Percent success of 95% confidence interval normal distribution: ", percentSuccess95Normal)
    print("Percent success of 99% confidence interval normal distribution: ", percentSuccess99Normal)
    print("Percent success of 95% confidence interval t-distribution: ", percentSuccess95t)
    print("Percent success of 99% confidence interval t-distribution: ", percentSuccess99t)
estimatingPopulationMean(120)
    
    
