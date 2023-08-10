import pandas as pds

df = pds.read_csv('user-churn.csv')
X = df.drop(columns = 'churned account status')
y = df['churned account status']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict value
y_test_pred = model.predict(X_test)
result_value = pds.DataFrame()
result_value['expected'] = list(y_test_pred)
result_value['actual'] = list(y_test)
print(result_value.head())

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_test_pred), model.score(X_test, y_test))

# Predict probability
y_test_pred_proba = model.predict_proba(X_test)
print(y_test_pred_proba[:5])
y_test_pred_proba_pretty = pds.DataFrame(y_test_pred_proba, columns = ['churn rate', 'retention rate'])
print(y_test_pred_proba_pretty.head())

# Check the parameter
print(model.coef_)
print(model.intercept_)

# Calculate the data manually
import numpy as np
for i in range(5):
    print(1 / (1 + np.exp(-(np.dot(X_test.iloc[i], model.coef_.T) + model.intercept_))))
    
# Check ROC and AUC
from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test, y_test_pred_proba[:, 1])
result = pds.DataFrame()
result['fpr'] = list(fpr)
result['tpr'] = list(tpr)
result['thres'] = list(thres)
print(result.head())

from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test, y_test_pred_proba[:, 1])
print(score)

import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()

# KS
fpr, tpr, thres = roc_curve(y_test, y_test_pred_proba[:, 1])
result = pds.DataFrame()
result['fpr'] = list(fpr)
result['tpr'] = list(tpr)
result['thres'] = list(thres)

plt.plot(thres[1:], tpr[1:])
plt.plot(thres[1:], fpr[1:])
plt.plot(thres[1:], tpr[1:] - fpr[1:])
plt.xlabel('Threshold')
plt.legend(['TPR', 'FPR', 'KS'])
plt.gca().invert_xaxis()
plt.show()
