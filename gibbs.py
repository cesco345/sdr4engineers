import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-np.pi,np.pi,5000)

sum = 0.5
n=1

while n < 100:
	sum = sum + np.divide(4,(2*n-1)*np.pi)*np.sin((2*n-1)*t)
	n=n+1

plt.plot(t,sum)

plt.show() 
