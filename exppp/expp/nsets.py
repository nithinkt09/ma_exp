from typing import Callable, Any
import numpy as np
import pandas as pd
import geopandas as gpd
import torch as torch
from sklearn.datasets import make_swiss_roll
from types import SimpleNamespace


class DynamicObject(SimpleNamespace):

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)


# get the data values as X and parameters that are used to generate that data values as t from swiss roll data
X, t = make_swiss_roll(n_samples=1000, random_state=42) #random value is set to ensure that the data generate has same random state everytime


# use dynamic object to represent data as swiss_roll.data and t value parameters as swiss_roll.parameters
swiss_roll = DynamicObject(data=X, parameters=t)

swiss_roll_set = {(tuple(row), param) for row, param in zip(swiss_roll.data, swiss_roll.parameters)}



# conver the dataset into a list of dictionaries with each dictionary mapping 3d coordinates to the parameter
data_list = [
    {'x': point[0], 'y': point[1], 'z': point[2], 't': param}
    for point, param in swiss_roll_set
]


# create a pandas dataframe with the dictionary where each column represents respective x, y, z, and t values
df = pd.DataFrame(data_list)