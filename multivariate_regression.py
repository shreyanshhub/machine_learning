#importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#reading data in a csv file
df = pd.read_csv("data.csv")

#imagine our data set has two independent variables , here in terms of columns in the csv file , let's say x_1 and x_2, dependent variable == y
X = df[["x_1","x_2"]]
y = df["y"]

#defining the model
model = linear_model.LinearRegression()
model.fit(X,y)

#predicting values , let's say coressponding to x_1 = 2 and x_2 = 3
prediction = model.predict([[2,3]])

#getting the weights in the model
weights = model.coef_
