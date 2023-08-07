X = [[1, 0], [5, 1], [6, 4], [4, 2], [3, 2]]
y = [-1, 0, 1, 1, 1]

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, y)

print(model.predict([[0, 0]]))
print(model.predict_proba([[0, 0]]))