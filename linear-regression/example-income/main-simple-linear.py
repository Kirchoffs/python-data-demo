import pandas as pds
df = pds.read_csv('IT-income.csv')
print(df.head())

X = df[['Working Years']]
Y = df['Salary']

from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Tahoma']

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X, Y)
print('Coefficient a:' + str(regr.coef_))
print('Intercept b:' + str(regr.intercept_))

plt.scatter(X, Y)
plt.plot(X, regr.predict(X), color = 'red')
plt.xlabel('Working Years')
plt.ylabel('Salary')

from sklearn.metrics import r2_score
r2 = r2_score(Y, regr.predict(X))
print("r2: ", r2)

import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
print(est.summary())

plt.show()
