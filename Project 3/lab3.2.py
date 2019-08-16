import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

rolls = 1000
success = []
prob = [0.2, 0.1, 0.15, 0.3, 0.2, 0.05]

p = prob[0] * prob[1] * prob[2]
q = 1 - p
for m in range(0,18):
    n = math.factorial(rolls)
    n_m = math.factorial(rolls-m)
    m_f = math.factorial(m)
    X = float((n/(m_f*n_m))*(p**m)*(q**(rolls-m)))
    success.append(X)
print("P=Prob(success in a single trial)=",p)
print("The expected number of success in n trials is", int(1000*p))

plt.stem(success)
plt.title('Bernoulli Trials: PMF - Binomial Formula')
plt.xlabel('Number of Successes in n=1000 trials')
plt.ylabel('Probability')
plt.xticks()
plt.show()
