from sklearn.metrics import confusion_matrix
import pandas as pds
import numpy as np

y_test = np.random.randint(2, size = 100)
y_test_pred = np.random.randint(2, size = 100)

result = confusion_matrix(y_test, y_test_pred)
print(result)
print()

result_table = pds.DataFrame(result, columns = ['Predicted 0', 'Predicted 1'], index = ['Actual 0', 'Actual 1'])
print(result_table)
print()

from sklearn.metrics import classification_report
print(classification_report(y_test, y_test_pred))