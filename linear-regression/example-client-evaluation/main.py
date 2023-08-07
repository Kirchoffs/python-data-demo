import pandas
df = pandas.read_excel('client-value.xlsx')
print(df.head())

X = df[['Historical Loan', 'Number of Loans', 'Education', 'Monthly Income', 'Gender']]
Y = df['Client Value']

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X, Y)
print('Coeficient: ' + str(regr.coef_))
print('Intercept: ' + str(regr.intercept_))

import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
print(est.summary())