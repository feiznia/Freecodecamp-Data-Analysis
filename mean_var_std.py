import numpy as np

def calculate(lst):

    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        mat = [lst[0:3],lst[3:6],lst[6:]]
        calculations = {
          'mean': [np.mean(mat, axis = 0), np.mean(mat, axis = 1),np.mean(lst)],
          'variance': [np.var(mat, axis = 0), np.var(mat, axis = 1), np.var(lst)],
          'standard deviation': [np.std(mat, axis = 0), np.std(mat, axis = 1), np.std(lst)],
          'max': [np.max(mat, axis = 0), np.max(mat, axis = 1), np.max(lst)],
          'min': [np.min(mat, axis = 0), np.min(mat, axis = 1), np.min(lst)],
          'sum': [np.sum(mat, axis = 0), np.sum(mat, axis = 1), np.sum(lst)]
        }
        return calculations
