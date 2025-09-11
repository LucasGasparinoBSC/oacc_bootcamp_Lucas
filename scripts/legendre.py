# Compute and plot the first few Legendre polynomials

import numpy as np
import matplotlib.pyplot as plt

# Define the Recursive Legendre Polynomial Function
def legendre(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2*n-1)*x*legendre(n-1, x) - (n-1)*legendre(n-2, x))/n
    
# Create a grid of x values between -1 and 1
x = np.linspace(-1, 1, 1000)

# For each n from 1 to 8, plot the Legendre polynomial on the same plot
plt.figure()
# Range n from 1 to 8
for i in range(1, 9):
    # At every x, compute the Legendre polynomial of order n
    y = [legendre(i, j) for j in x]
    # Plot the Legendre polynomial of order n
    plt.plot(x, y, label=f'n={i}')

plt.legend()
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.title('Legendre Polynomials')
plt.grid()
plt.show()