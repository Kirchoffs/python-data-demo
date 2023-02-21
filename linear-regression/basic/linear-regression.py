import matplotlib.pyplot as plt

X = [[1], [2], [4], [5]]
Y = [2, 4, 6, 8]
plt.scatter(X, Y)

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X, Y)
print('Coefficient a:' + str(regr.coef_[0]))
print('Intercept b:' + str(regr.intercept_))

y = regr.predict([[1.5], [2.5], [4.5]])
print(y)
plt.plot(X, regr.predict(X))
plt.show()

