import numpy as np

def wrapper(measure, Y, Y_predicted, qids):
    Y = np.mat(Y)
    Y_predicted = np.mat(Y_predicted)
    qids_perfs = []
    for inds in qids:
        Y_sub = Y[inds]
        Y_predicted_sub = Y_predicted[inds]
        perfs = measure.getPerformance(Y_sub, Y_predicted_sub)
        qids_perfs.append(perfs)
    #quite a bit juggling follows to handle the fact, that nans encode
    #queries for which performance is undefined (happens sometimes
    #in ranking
    #
    #count the number of non-nan values in each column
    perfs = np.vstack(qids_perfs)
    normalizers = np.isnan(perfs)
    normalizers = np.logical_not(normalizers)
    normalizers = np.sum(normalizers, axis=0)
    normalizers = np.where(normalizers>0,normalizers,np.nan)
    #turns nans into zeroes
    perfs = np.nan_to_num(perfs)
    perfs = np.sum(perfs, axis=0)
    perfs = perfs/normalizers
    return perfs


def aggregate(performances):
    normalizer = np.sum(np.logical_not(np.isnan(performances)))
    if normalizer == 0:
        return np.nan
    else:
        performances = np.nan_to_num(performances)
        return np.sum(performances)/normalizer
    
def multitask(Y, P, f):
    perfs = []
    for i in range(Y.shape[1]):
        perfs.append(f(Y[:,i], P[:,i]))
    return perfs
    
class UndefinedPerformance(Exception):
    """Used to indicate that the performance is not defined for the
    given predictions and outputs."""
    #Examples of this type of issue are disagreement error, which
    #is undefined when all the true labels are the same, and
    #recall, which is not defined if there are no relevant
    #instances in the data set.

    def __init__(self, value):
        """Initialization
        
        @param value: the error message
        @type value: string"""
        self.value = value

    def __str__(self):
        return repr(self.value)
