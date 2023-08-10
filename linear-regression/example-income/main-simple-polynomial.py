import pandas as pds
import matplotlib.pyplot as plt
df = pds.read_csv('IT-income.csv')
print(df.head())

X = df[['Working Years']]
Y = df['Salary']

from sklearn.preprocessing import PolynomialFeatures
regr_processor = PolynomialFeatures(degree = 2)
X_polynomial = regr_processor.fit_transform(X)

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X_polynomial, Y)
print(regr.coef_)
print(regr.intercept_)

plt.scatter(X, Y)
plt.plot(X, regr.predict(X_polynomial), color = 'red')

import statsmodels.api as sm
X2_polynomial = sm.add_constant(X_polynomial)
est = sm.OLS(Y, X2_polynomial).fit()
print(est.summary())

plt.show()
