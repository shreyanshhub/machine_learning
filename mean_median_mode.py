import numpy as np
from scipy import stats

data = [1,2,3,4,5,6,6,7,9,10]

#calculation of mean
mean = np.mean(data)

#calculation of median
median = np.median(data)

#calculation of mode
mode = stats.mode(data)

