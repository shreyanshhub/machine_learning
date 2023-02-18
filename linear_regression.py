#importing modules
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#generating data
x = np.random.uniform(1.0,10.0,250)
y = np.random.uniform(5.0,28.0,250)

#getting the regression line parameters
m,c,r,p,std = stats.linregress(x,y)

#generating predicted y values
def pred_y(x):
  return m*x + c

y_pred = list(map(pred_y,x))

#plotting the regression line and the data points
plt.scatter(x,y)
plt.plot(x,y_pred)
plt.show()
