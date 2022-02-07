
import matplotlib.pyplot as plt

x = int(input("Enter x: "))
w = [x]
count = 0
c = []

def collatz(x):
    while x != 1:
        if x%2==1:
            x = 3*x+1
            w.append(x)
        else:
            x = x//2
            w.append(x)
    return w

a = collatz(x)
print(a)
print(type(a))

for i in a:
    count += 1
    c.append(count)
print(c)


plt.xlabel("Number of Iterations")
plt.ylabel("Output for Iteration(x)")
plt.title("Collatz Conjecture for n")
plt.plot(c, w, "bo-")
plt.show()














