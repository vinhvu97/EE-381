# Vinh Vu, 015347252
# Lab 4, Problem 1.2
# Exponential R.V

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


beta = 40
n = 10000
t = np.random.exponential(beta,n)

# Create bins and histograms
nbins = 30
edgecolor = 'w'
bins = [float(t) for t in np.linspace(0,200,nbins+1)]
h1, bin_edges = np.histogram(t,bins, density=True)

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
def ExpPDF(beta,t):
    f=np.exp((-1/beta)*t)*(1/beta)
    return f

f=ExpPDF(beta,b1)
plt.plot(b1,f,'r')
plt.title("Exponential Random Variable")
plt.xlabel("n=10000")
plt.ylabel("Probability")
plt.show()

#calculate the mean and std
mu_x = np.mean(t)
sig_x = np.std(t)
print("mu_x=",mu_x)
print("sig_x=",sig_x)


