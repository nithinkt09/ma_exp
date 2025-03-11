from typing import Callable, Union
import pandas as pd
import geopandas as gpd


class Object:

    def __init__(self, data: Union[pd.DataFrame, gpd.GeoDataFrame]):
        self.data = data

    def transform(self, fn):
        morphism = Morphism(self.data, fn)
        return morphism.target



class Morphism:
    
    def __init__(self, source, fn):
        self.source = source
        self.fn = fn
        self.target = fn(source)


    
class Category:
    
    def __init__(self, objects, morphisms):
        self.objects = objects
        self.morphisms = morphisms

    

class HomSet:
    def __init__(self, source, target, morphisms):
        self.source = source
        self.target = target
        self.morphism = morphisms