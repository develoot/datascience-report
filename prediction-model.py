#!/usr/bin/env python

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas

df = pandas.read_csv('data.csv')
df.head()

# split data into trainig and testing sets
x_train = df['time'][:len(df['time'])//2]
y_train = df['cputime'][:len(df['cputime'])//2]

x_test = df['time'][len(df['time'])//2:]
y_test = df['cputime'][len(df['cputime'])//2:]

regr = linear_model.LinearRegression()
regr.fit(x_train.values.reshape(-1,1), y_train)

y_pred = regr.predict(x_test.values.reshape(-1,1))

print("Coeff: \n", regr.coef_)
print("MSE: %.2f" % mean_squared_error(y_test, y_pred))
print("Coeff of Determination: %.2f" % r2_score(y_test, y_pred))

plt.scatter(x_test.values.reshape(-1,1), y_test, color="black")
plt.plot(x_test.values.reshape(-1,1), y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
