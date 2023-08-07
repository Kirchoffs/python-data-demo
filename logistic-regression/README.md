# Notes
## Transform
> y -> e^y -> e^y / (1 + e^y) -> 1 / (1 + e^(-y))

## ROC
### Confision Matrix
|                  | Positive(Predicted) | Negative(Predicted) |
| ---------------- | ------------------- | ------------------- |
| Positive(Actual) | TP                  | FN                  |
| Negative(Actual) | FP                  | TN                  |  

```
TPR = TP / (TP + FN)

FPR = FP / (FP + TN)
```

## sklearn.linear_model.LogisticRegression
predict_proba(X)

The returned estimates for all classes are ordered by the label of classes.

For a multi_class problem, if `multi_class` is set to be "multinomial" the softmax function is used to find the predicted probability of each class. Else ("ovr") use a one-vs-rest approach, i.e calculate the probability of each class assuming it to be positive using the logistic function. and normalize these values across all the classes.