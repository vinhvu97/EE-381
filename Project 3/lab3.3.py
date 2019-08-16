import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

rolls = 1000
success = []
prob = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
p = prob[0] * prob[1] * prob[2]
lamda = rolls * p

for m in range(0,18):
    X = ((lamda**m)*(math.exp(-1*lamda)))/(math.factorial(m))
    success.append(X)

plt.stem(success)
plt.title('Bernoulli Trials: PMF - Poisson Approximation')
plt.xlabel('Number of Successes in n=1000 trials')
plt.ylabel('Probability')
plt.xticks()
plt.show()
