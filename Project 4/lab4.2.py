import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Generate the values of the RV X
nbooks = 15
N = 10000
a = 1.0
b = 4.0
mu_x = (a+b)/2
sig_x = np.sqrt((b-a)**2/12)
X = np.zeros((N,1))
for k in range(0,N):
    x = np.random.uniform(a,b,nbooks)
    w = np.sum(x)
    X[k] = w

# Create bins and histogram
nbins = 30
edgecolor = 'w'
bins = [float(x) for x in np.linspace(nbooks*a,nbooks*b,nbins+1)]
h1, bin_edges = np.histogram(X,bins, density=True)

# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges)-1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1+be2)/2
barwidth = b1[1]-b1[0]
plt.close('all')

# Plot the bar graph
fig1 = plt.figure(1)
plt.bar(b1,h1,width=barwidth,edgecolor=edgecolor)

#Plot the Gaussian Function
def gaussian(mu,sig,z):
    f = np.exp(-(z-mu) ** 2/(2 * sig ** 2))/(sig * np.sqrt(2 * np.pi))
    return f

def uniform_pdf(a,b,x):
    f = (1/abs(b-a))*np.ones(np.size(x))
    return f

if (nbooks == 1):
    f = uniform_pdf(a,b,b1)
    plt.plot(b1,f,'r')
    plt.title("PDF of book stack height and comparison with Gaussian")
    plt.xlabel("Book stack height for n=1 book")
    plt.ylabel("Probability")
    plt.show()
    mu_x = np.mean(x)
    sig_x = np.std(x)
    print("nbooks=",nbooks)
    print("mu_x=",mu_x)
    print("sig_x=",sig_x)
else:
    f = gaussian(mu_x * nbooks,sig_x * np.sqrt(nbooks),b1)
    plt.plot(b1,f,'r')
    plt.title("PDF of book stack height and comparison with Gaussian")
    plt.xlabel("Book stack height for n=15 books")
    plt.ylabel("Probability")
    plt.show()

    # Calculate the mean and std
    mu_x = np.mean(x)*nbooks
    sig_x = np.std(x)*np.sqrt(nbooks)
    print("nbooks=",nbooks)
    print("mu_x=",mu_x)
    print("sig_x=",sig_x)

