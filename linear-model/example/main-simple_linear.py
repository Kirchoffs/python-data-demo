import pandas as pds
df = pds.read_excel('IT Income.xlsx')
print(df.head())

X = df[['Working Years']]
Y = df['Salary']

from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Tahoma']

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X, Y)
print('Coefficient a:' + str(regr.coef_[0]))
print('Intercept b:' + str(regr.intercept_))

plt.scatter(X, Y)
plt.plot(X, regr.predict(X), color = 'red')

plt.xlabel('Working Years')
plt.ylabel('Salary')
plt.show()

