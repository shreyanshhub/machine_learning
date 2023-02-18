#creating our own data

import numpy as np
import matplotlib.pyplot as plt

#this will generate 1000 random floats between 0 and 10
data = np.random.uniform(0.0,10.0,1000)

#plotting this data on a histogram 
plt.hist(data,5)
plt.show() 
