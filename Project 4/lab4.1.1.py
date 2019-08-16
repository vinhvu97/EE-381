# Vinh Vu, 015347252
# Lab 4, Problem 1.1
# Uniform R.V

import numpy as np
import random
import string
import matplotlib
import matplotlib.pyplot as plt

a = 1.0
b = 4.0
n = 10000
x = np.random.uniform(a,b,n)

# Create bins and histograms
nbins = 30
edgecolor = 'w'
bins = [float(x) for x in np.linspace(a,b,nbins+1)]
h1, bin_edges = np.histogram(x,bins, density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges)-1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1]-b1[0]
plt.close('all')

# Plot the bar graph
fig1 = plt.figure("Uniform Random Variable")
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

# Plot the uniform pdf
def UnifPDF(a,b,x):
    f = (1/abs(b-a))*np.ones(np.size(x))
    return f
f=UnifPDF(a,b,b1)
plt.plot(b1,f,'r')
plt.title("Uniform Random Variable")
plt.xlabel('n=10000')
plt.ylabel('Probability')
plt.show()

#calculate the mean and std
mu_x = np.mean(x)
sig_x = np.std(x)                           
print("mu_x =",mu_x)
print("sig_x =",sig_x)

