import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Generate the values of the RV X
beta = 40
nbat = 24
n=10000
C=np.zeros((n,1))
for i in range (0,n):
    t = np.random.exponential(beta,nbat)
    w=np.sum(t)
    C[i]=w

# Create bins and histogram
nbins=30 
edgecolor='w' 
bins=[float(t) for t in np.linspace(min(C),max(C),nbins+1)]
h1, bin_edges = np.histogram(C,bins,density=True)

# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1]
be2=bin_edges[1:np.size(bin_edges)]
b1=(be1+be2)/2
barwidth=b1[1]-b1[0] 
plt.close('all')

# Plot the bar graph
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

# Plot the uniform PDF
def gaussian(mu, sig, z):
    f = np.exp(-(z - mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
    return f

mu = nbat * beta
sig = beta * (np.sqrt(nbat))
f = gaussian(mu,sig,b1)
plt.plot(b1,f,'r')

plt.title('PDF of Lifetime of a 24 battery carton and comparison with Gaussian')
plt.xlabel('Lifetime of a 24 batteries carton')
plt.ylabel('Probability')    
plt.show()


fig2 = plt.figure(1)
h2 = np.cumsum(h1)*barwidth
plt.bar(b1,h2, width=barwidth, edgecolor = edgecolor)
plt.title('CDF of lifetime of a 24 batteries carton')
plt.xlabel('Lifetime of a 24 batteries carton')
plt.ylabel('Probability')
plt.show()

# Calculate the mean and std
mu_C=np.mean(C)
print("mu_c=",mu_C)
sig_C=np.std(C)
print("sig_c=",sig_C)

