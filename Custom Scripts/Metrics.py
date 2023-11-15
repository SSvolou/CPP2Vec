"""In this script we define all the functions of the metrics that we used in our study."""

import numpy as np
import sklearn.metrics as metrics
from sklearn.metrics import confusion_matrix
import scipy.stats
import math

#y_true represents the ground truth values and y_prob the probability estimates.

# Computes Sensitivity Metric
def sensitivity(y_true, y_prob, thresh=0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_prob).ravel()
    return tp / (tp + fn)

# Computes Specificity Metric
def specificity(y_true, y_prob, thresh=0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_prob).ravel()
    return tn / (tn + fp)

# Computes Accuracy Metric
def accuracy(y_true, y_prob, thresh=0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    return metrics.accuracy_score(y_true, y_prob)

# Computes Area Under the Curve Metric
def AUC(y_true, y_prob):
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    return metrics.roc_auc_score(y_true, y_prob)

# Computes Matthews Correlation Coefficient Metric
def MCC(y_true, y_prob, thresh=0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    return metrics.matthews_corrcoef(y_true, y_prob)

# Computes the Confusion Matrix
def confusion_matrix(y_true,y_prob, thresh = 0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    tn, fp, fn, tp = confusion_matrix(y_true, y_prob).ravel()
    return tn, fp, fn, tp

# Computes Precision Metric
def precision(y_true, y_prob, thresh = 0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    return metrics.precision_score(y_true,y_prob)

# Computes Recall Metric
def recall(y_true, y_prob, thresh = 0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    return metrics.recall_score(y_true,y_prob)

# Computes F1-Score Metric
def f1(y_true, y_prob, thresh = 0.8):
    y_true = np.array(y_true)
    y_prob = (np.array(y_prob) + 1 -thresh).astype(np.int16)
    return metrics.f1_score(y_true,y_prob)

# Computes Area Under the Precision-Recall Curve Metric
def AUPRC(y_true, y_prob):
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    return metrics.average_precision_score(y_true, y_prob)

# Computes Spearman's Correlation Coefficient Metric
def spearman(y_true, y_prob):
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    return scipy.stats.spearmanr(y_true, y_prob)

# Computes Pearson's Correlation Coefficient Metric
def pearson(y_true, y_prob):
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    return scipy.stats.pearsonr(y_true, y_prob)

# Computes Root Mean Square Error Metric
def rmse(y_true, y_prob):
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    return math.sqrt(metrics.mean_squared_error(y_true, y_prob))

# Computes R2-Score Metric
def r2(y_true, y_prob):
    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    return metrics.r2_score(y_true, y_prob) 
