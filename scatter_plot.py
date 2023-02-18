#plotting a scatter plot 

import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(1,100,50)
y = np.random.uniform(4,56,50)

plt.scatter(x,y)
plt.show()
