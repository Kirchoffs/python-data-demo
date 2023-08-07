from sklearn.tree import DecisionTreeRegressor

X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]

model = DecisionTreeRegressor(max_depth = 2, random_state = 0)
model.fit(X, y)

print(model.predict([[5, 5], [7, 7], [9, 9]]))
