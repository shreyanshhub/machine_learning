#importing modules
import numpy as np
import matplotlib.pyplot as plt

#generating random data
x = np.random.uniform(1.0,28.0,25)
y = np.random.uniform(24.0,85.0,25)

#defining 3rd degree polynomial regression model
model = np.poly1d(np.polyfit(x,y,3))

#generating a line to plot the proper 3rd degree curve despite of having "x"
axis = np.linspace(1.0,28.0,1000)

#plotting the 3rd degree curve
plt.scatter(x,y)
plt.plot(axis,model(axis))
plt.plot()
