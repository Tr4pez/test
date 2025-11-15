import matplotlib.pyplot as plt
import numpy as np

a = input("what is 'a': ")
b = input("what is 'b': ")
x = np.arange(-10,10,0.1)
y = float(a)*x+float(b)
plt.plot(x,y)
plt.show()


