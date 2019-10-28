# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html

# Library to calculate AUC 
import numpy as np
from sklearn.metrics import roc_auc_score

y_true = np.array([0, 1, 1,1, 1,1])
y_scores = np.array([0.5, 0.2, 0.7, 0.1, 0.9,0.4])
print(roc_auc_score(y_true, y_scores))


# to look at / calculate ROC curve specifically:
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html
