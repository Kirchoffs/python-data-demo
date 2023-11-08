# Notes

## matplotlib
```
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```

The 111 is shorthand telling Matplotlib that we want a grid of 1 × 1 and that the current plot should go in index 1 of that grid.

## K Fold Cross Validation
```
from sklearn.model_selection import cross_val_score

acc = cross_val_score(model, X, y, cv = 5)

acc = cross_val_score(model, X, y, scoring = 'roc_auc', cv = 5)
```
