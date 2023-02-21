X = [[1, 0], [5, 1], [6, 4], [4, 2], [3, 2]]
Y = [0, 1, 1, 0, 0]

from sklearn.linear_model import LogisticRegression
regr = LogisticRegression()
regr.fit(X, Y)
print(regr.coef_)
print(regr.intercept_) # P = 1 / (1 + e ^ (-(k0 + k1x1 + k2x2)))

x = [[2, 2], [3, 1]]
x_predict = regr.predict(x)
x_predict_proba = regr.predict_proba(x)

print(x_predict)
print(x_predict_proba)
