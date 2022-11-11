import numpy as np
import matplotlib.pyplot as plt
n =  int(input("Введите количество чисел:"))
numbx = np.zeros(n)
numby = np.zeros(n)
fib1 = fib2 = 1
numbx[0] = fib1
numbx[1] = fib2
for i in range(2,n):
    fib1, fib2 = fib2, fib1 + fib2
    numbx[i]=fib2
count = 1
for i in range(n):
    numby[i]=i+1
print(numbx)

plt.scatter(numbx, numby)
graph1 = plt.plot(numbx, numby)
grid1 = plt.grid(True)
plt.show()