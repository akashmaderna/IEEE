import numpy as np, matplotlib.pyplot as plt#call the numpy and matplotlib modules
x = np.linspace(-4,4,1000)#generates 1000 random values for calculation between -4 and 4
y = np.exp(-x**2/2)/np.sqrt(2*np.pi)#calculates probablity density(normal distribution) of 1000 randomly generated values
plt.scatter(x, y)#plots a scatter graph of the numbers and their normal distribution values
plt.title ('Normal Distribution')#labels the graph
plt.xlabel('X')#labels the x=axis
plt.ylabel('Probablity Distrbution')#labels the y-axis
plt.show()#shows the graph
