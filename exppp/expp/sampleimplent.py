import pandas as pd
import geopandas as gpd
import copy
import numpy as np
from typing import Union, Dict, Set, Callable, Any, List

class DataObject:

    """
    CatsObject class represents an abstractform of raw data as an object
    this wraps data (pandas dataframe or geopandas dataframe) and extracts metadata

    here, the data is assumed to be in a tabular (could be extracted to spatial) form 
    
    """

    def __init__(self, data: Union[pd.DataFrame, gpd.GeoDataFrame]):

        """
        data is expected to be either pandas or geopandas dataframe
        """
        self.data = data
        self.metadata = self._extract_metadata() # extracts metadata: number of rows, columns, columnnames, datatypes, etc.

    
    def _extract_metadata(self) -> Dict:
        """
        uses built-in dataframe methods to extract:
            - number of rows or samples: shape[0]
            - number of columns or features: shape[1]
            - column names: .cloumns.tolist()
            - dictionary that maps each column to its data type
        """

        metadata = {
            'num_rows': self.data.shape[0], # number of samples
            'num_columns': self.data.shape[1], # number of features
            'columns': self.data.columns.to_list(), # column names
            'data_types': self.data.dtype.to_dict() # each columnn name acts as a key and datatype as value       

        }
        return metadata
    
    def __repr__(self):
        # a string representation of the CatsObject
        return f"DataObject(metadata) = {self.metadata}"

class Category:
    """
    category class represents abtract category with data objects and morphisms between them
    
    this class keeps a collection of data objects and set of morphisms between any two objects

    morphisms (transformations, functions, or methods) takes one dataobject and returns a new dataobject, 
    each morphism is represented as a dictionary keyed with it's id(source) and id(target) and values as respective methods and description
    """
    def __init__(self):
        self.objects: Set[DataObject] = set() # objects are stored in set for uniquness
        self.morphisms = set({}) # set of morphisms 


    def add_object(self, obj: DataObject):
        """
        adds a new object to the category, an ideneity map, Hom(A, A) are automatically added
        """
        self.add_object.add(obj)
    

class Morphism:

    """
    morphism class represents a tranformation that takes a source object and create a new object based on the defined rule or method
    """

    def __init__(self, source: DataObject, fn: Callable[[DataObject], DataObject], description: str = "morphism"):

        self.source = source # source object
        self.fn = fn # morphism or transformation on the source object
        self.description = description # description of the morphism
        self.target = self.fn(source)

    
    def __repr__(self) -> str:
        # a string representation showing the source, target, and description
        return f"Morphism({self.source} -> {self.target}, description = {self.description})"
    


class HomSet:
    """
    Homset class represents set of all morphisms between any two objects of a given category
    source: domain, target: codomain, morphisms: list of all morphisms between domain and codomain
    """
    def __init__(self, source: DataObject, target: DataObject):
        self.source = source # source or domain of the HomSet
        self.target = target # target or codomain of the HomSet
        self.morphisms: Set[Morphism] = set() # set of all morphisms between source and target


    
    def add_morphism(self, morphism: Morphism) -> None:
        """
        any morphism in the homset must have the same source and target
        """
        if morphism.source != self.source or morphism.target != self.target:
            raise ValueError("Morphism's source and target must match Homset's source and target")
        self.morphisms.add(morphism)

    def __repr__(self):
        return f"HomSet({self.source}, {self.target}, morphism = {self.morphisms})"