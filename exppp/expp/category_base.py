import pandas as pd
import geopandas as gpd
from typing import Union, Set

class Object:
    def __init__(self, data: Union[pd.DataFrame, gpd.GeoDataFrame]):
        # validate the input data
        if not isinstance(data, (pd.DataFrame, gpd.GeoDataFrame)):
            raise TypeError("input data must be of type pandas DataFrame or geonPandas GeoDataFrame")
        
        self.data = data
        self.outgoing: Set[Morphimn] = set()
        self.incoming: Set[Morphimn] = set()


    def __repr__(self):
        return f"Object({self.data.__class__,__name__})"


class Morphimn:
    pass