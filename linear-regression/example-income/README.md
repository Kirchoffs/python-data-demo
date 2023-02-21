# Notes

## Required Modules
- pandas
- matplotlib
- sklearn
- statsmodels

## Matplotlib Notes
For font related info, use `plt.rcParams.keys()` to get the basic idea.

## Evaluation
- R-squared
- Adjacent R-squared
- P

### R-squared
- TSS: Total Sum of Squares
- RSS: Residual Sum of Squares
- ESS: Explained Sum of Squared

```
TSS = sum((Y_i - Y_mean) ^ 2)
RSS = sum((Y_i - Y_fitted) ^ 2)
ESS = sum((Y_fitted - Y_mean) ^ 2)

TSS = RSS + ESS

R-squared = 1 - RSS / TSS
Adjacent R-squared = 1 - (1 - R-squared) (n - 1) / (n - k - 1)
```