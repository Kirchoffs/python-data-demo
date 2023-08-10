= Notes

== Gini Coefficient
$ "gini"(T) = 1 - sum_(i=0)^n p_i^2 $
$ "gini"_A (T) = S_1/(S_1 + S_2) "gini"(T_1) + S_2/(S_1 + S_2) "gini"(T_2) $

== Information Entropy
$ "H"(X) = -sum_i p_i log_2(p_i) $
$ "H"_A (X) = S_1/(S_1 + S_2) H(X_1) + S_2/(S_1 + S_2) H(X_2) $

== Information Gain
$ "Gain"(A) = H(X) - H_A (X) $

== Regression Decision Tree
It uses MSE as the split criteria, instead of Gini or Entropy.

$ "MSE" = 1/n sum(y^"(i)" - accent(y, hat)^"(i)") $