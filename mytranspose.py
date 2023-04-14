import numpy as np
import pandas as pd

def mytranspose(x):
    # print(x)
    y= np.ones((x.shape[1],x.shape[0]))
    
    for i in range(y.shape[0]):
        for j in range(y.shape[1]):
            y[i,j] = x[j,i]
    
    return y


def mytransposeForDataFrame(x):
    y = pd.DataFrame(index = x.columns, columns = x.index)
    
    
    for i in range(y.shape[0]):
        for j in range(y.shape[1]):
            y.iloc[i][j] = x.iloc[j][i]
    return y