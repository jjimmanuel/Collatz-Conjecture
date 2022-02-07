
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = int(input("Enter x: "))

w = []

def collatz(x):
    while x > 1:
        w.append(x)
        if x%2==1:
            x = 3*x+1
        else:
            x = x//2
    if x == 1:
        w.append(x)
    return w


functions = [collatz(x)]
y = {'Index': count(len(collatz(x))),  'Collatz Sequence': functions[0]}
z = pd.DataFrame(y)
print(z)

a = z['Index']
b = z['Collatz Sequence']
plt.scatter(a, b)
plt.show()


















