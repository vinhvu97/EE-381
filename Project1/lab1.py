import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import string

#Number 1
def nSidedDie(p):
    if sum(p) != 1:
        print('Probability values are incorrect!')
    sides = len(p)
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = np.random.rand()
    for k in range(0,sides):
        if r > cp[k] and r<= cp[k+1]:
            sides = k+1
    return sides
p = [0.1,0.15,0.20,0.05,0.30,0.10,0.10]
N_1 = 10000
test_1 = []
for j in range(0,N_1):
    r = nSidedDie(p)
    test_1.append(r)

b=range(1,9)
sb=len(b)
h1, bin_edges = np.histogram(test_1,bins=b)
b1=bin_edges[0:sb-1]
    
fig1 = plt.figure(1)
plt.stem(b1,h1)
plt.title('Stem plot - Rolling N-Sided Die')
plt.xlabel('Die Side')
plt.ylabel('Number of Occurences')
plt.show()

fig2=plt.figure(2)
p1=h1/N_1
plt.stem(b1,p1)
plt.title('Stem plot - Rolling N-Sided Die Probability')
plt.xlabel('Die Side')
plt.ylabel('Probability')
plt.show()

 #Number 2
def SumOfSeven():
    sum_7 = 0
    iteration = 0
    while sum_7 != 7:
        d1 = np.random.randint(1,7)
        d2 = np.random.randint(1,7)
        iteration+=1
        sum_7=d1+d2
    return iteration
test2 = []
r = SumOfSeven()
print("Numer of rolls to achieve sum equal to 7:",r)
N_2 = 100000
for i in range(0,N_2):
    r = SumOfSeven()
    test2.append(r)
    
b=range(1,25)
sb=len(b)
h1, bin_edges = np.histogram(test2,bins=b)
b1=bin_edges[0:sb-1]
    
fig1 = plt.figure(1)
plt.stem(b1,h1)
plt.title('Stem plot - Sum of two dice ')
plt.xlabel('Number of Rolls')
plt.ylabel('Number of Occurences')
plt.xticks(b1)
plt.show()

fig2=plt.figure(2)
p1=h1/N_2
plt.stem(b1,p1)
plt.title('Stem plot - Sum of two dice: Probability')
plt.xlabel('Number of Rolls')
plt.ylabel('Probability')
plt.xticks(b1)
plt.show()

#Number 3
s_3 = []
def coinFlip():
    head = 0
    success = 0
    for k in range(100):
        flip = np.random.randint(1,3)
        if flip == 1:
            head+=1
    if head == 50:
        success += 1
    return success

flip1 = coinFlip()
if flip1 == 1:
    print('Success!')
else:
    print('Fail!')

for i in range(0,N_2):
    times = coinFlip()
    if times == 1:
        s_3.append(times)
rate = len(s_3)/N_2
print('The success probability is',rate)

#Number 4

def passMatch(k):
    password=[]
    for i in range(k*80000):
        word = ''
        for j in range(4):
            let=random.choice(string.ascii_lowercase)
            word+=let
        password.append(word)
    return password

matching = passMatch(1)
success_rate1 = []
success_rate7=[]
for k in range(1000):
    success = 0
    my_pass = ''
    for j in range(4):
        my_letter = random.choice(string.ascii_lowercase)
        my_pass += my_letter
    for i in range(len(matching)):
        if my_pass == matching[i]:
            success+=1
    if success != 0:
        success_rate1.append(success)
rate = len(success_rate1)/1000
print("The success rate of matching password for m:",rate)

matching2 = passMatch(7)
for k in range(1000):
    success = 0
    my_pass = ''
    for j in range(4):
        my_letter = random.choice(string.ascii_lowercase)
        my_pass += my_letter
    for i in range(len(matching2)):
        if my_pass == matching2[i]:
            success+=1
    if success != 0:
        success_rate7.append(success)
rate = len(success_rate7)/1000
print("The success rate of matching password for k*m:",rate)

