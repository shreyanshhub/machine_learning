#generating data drawn from normal distribution

import numpy as np

#random 1000 values with mean 6 and std 1 

data = np.random.normal(6.0,1.0,1000)

#plotting a histogram with 100 histogram bars
plt.hist(data,100)
plt.show()
