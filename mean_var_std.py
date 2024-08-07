import numpy as np

def calculate(lst):

    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        mat = np.vstack([lst[0:3],lst[3:6],lst[6:]])
        calculations = {
          'mean': [np.mean(mat, axis = 0).tolist(), np.mean(mat, axis = 1).tolist(), np.mean(lst)],
          'variance': [np.var(mat, axis = 0).tolist(), np.var(mat, axis = 1).tolist(), np.var(lst)],
          'standard deviation': [np.std(mat, axis = 0).tolist(), np.std(mat, axis = 1).tolist(), np.std(lst)],
          'max': [np.max(mat, axis = 0).tolist(), np.max(mat, axis = 1).tolist(), np.max(lst)],
          'min': [np.min(mat, axis = 0).tolist(), np.min(mat, axis = 1).tolist(), np.min(lst)],
          'sum': [np.sum(mat, axis = 0).tolist(), np.sum(mat, axis = 1).tolist(), np.sum(lst)]
        }
        return calculations
