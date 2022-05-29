'''
very easy model

'''


import numpy as np
import pandas as pd
import plotly.graph_objects as go

class hysteresis_model:
    def __init__(self,y):
        
        self.y_data = y
        self.location = []

        tangle = []
        limit = max(y)-min(y)

        for i in range(len(y)-1):
            data = abs(y[i+1]-y[i])
            tangle.append(abs(y[i+1]-y[i]))
            if data > limit/2:
                self.location.append(i)
        
    def analyse(self):
        if len(self.location) > 2:
            return False
        else :
            return True

    def fit_data(self):
        new_y = []
        fit_curve_a = (np.mean(self.y_data[:self.location[0]+1])+np.mean(self.y_data[self.location[1]+1:]))/2
        fit_curve_b = np.mean(self.y_data[self.location[0]+1:self.location[1]])
        for _ in range(self.location[0]+1):
            new_y.append(fit_curve_a)
        for _ in range(self.location[1]-self.location[0]):
            new_y.append(fit_curve_b)
        for _ in range(len(self.y_data)-self.location[1]-1):
            new_y.append(fit_curve_a)
        return new_y


        