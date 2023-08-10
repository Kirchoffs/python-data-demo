import pandas as pd

df = pd.read_csv('employee-resign-data.csv')
print(df.head())
print()

df = df.replace({'Salary': {'low': 1, 'medium': 2, 'high': 3}})

X = df.drop(columns = 'Resignation')
y = df['Resignation']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 1)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth = 3, random_state = 42)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
print()

y_test_pred = model.predict(X_test)
res = pd.DataFrame()
res['expected'] = list(y_test)
res['actual'] = list(y_test_pred)
print(res.head())
print()

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test_pred, y_test))
print()

y_test_pred_proba = model.predict_proba(X_test)
print(type(y_test_pred_proba))
proba_res = pd.DataFrame(y_test_pred_proba, columns = ['stay', 'resign'])
print(proba_res.head())
print()

from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test, y_test_pred_proba[:, 1])
roc = pd.DataFrame()
roc['fpr'] = list(fpr)
roc['tpr'] = list(tpr)
roc['thres'] = list(thres)

import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
plt.show()

from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, y_test_pred_proba[:, 1]))

features = X.columns
importances = model.feature_importances_
importances_df = pd.DataFrame()
importances_df['features'] = list(features)
importances_df['importances'] = list(importances)
importances_df = importances_df.sort_values(by = 'importances', ascending = False)
print(importances_df)