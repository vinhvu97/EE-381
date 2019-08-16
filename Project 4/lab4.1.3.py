# Vinh Vu, 015347252
# Lab 4, Problem 1.3
# Normal R.V

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

mu=2.5
sigma=0.75
n=10000
x = np.random.normal(mu,sigma,n)

# Create bins and histograms
nbins = 30
edgecolor = 'w'
bins = [float(t) for t in np.linspace(1,4,nbins+1)]
h1, bin_edges = np.histogram(x,bins, density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges)-1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1]-b1[0]
plt.close('all')

# Plot the bar graph
fig1 = plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)


# Plot the uniform pdf
def NormPDF(mu,sigma,z):
    f=np.exp(-(z-mu)**2/(2**sigma**2))*(1/(sigma*np.sqrt(2*np.pi)))
    return f

f=NormPDF(mu,sigma,b1)
plt.plot(b1,f,'r')
plt.title("Normal Random Variable")
plt.xlabel("n=10000")
plt.ylabel("Probability")
plt.show()

# Calculate the mean and std
mu_x = np.mean(x)
sig_x = np.std(x)
print("mu_x=",mu_x)
print("sig_x=",sig_x)


