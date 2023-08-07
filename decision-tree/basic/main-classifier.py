from sklearn.tree import DecisionTreeClassifier

X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 0, 0, 1, 1]

model = DecisionTreeClassifier(random_state = 0)
model.fit(X, y)

print(model.predict([[5, 5], [7, 7], [9, 9]]))
      