
from pyarrow import feather
import numpy as np
import pandas as pd

""" Safe Drugs Data Retrieval Library """

class file_connector:
    """ 
    read data from filesystem
    args:
        datafile: path to feather-formatted file
    """
    
    def __init__(self, datafile):
        self.datafile = datafile
        self.data = feather.read_feather(source=datafile, nthreads=16)
        

    def unique_values(self, column):
        uniq_vals = self.data[column].unique()
        uniq_vals = uniq_vals[np.argsort(uniq_vals)]
        return uniq_vals
        

    def counts_by_feature(feature, query=""):
        """
        return outcomes data counts for a given feature, e.g. report_year, age_category, drug_category.
        if "query" is provided, will first filter the dataset on that query string.
        inputs:
            feature: column name you'd like to group on, e.g. "gender_code", "report_year"
            query (optional): optional query string to filter the dataset, e.g. 'gender_code == "F"'
        returns:
            struct of this format: {series: array, x: array, y: array, y_norm:array}
        example:
            foo = counts_by_feature("report_year", 'gender_code == "M"')
        """

        ds = data.query(query) if query else data
                  
        series = (ds.groupby([feature])
                  .apply(lambda x : x.shape[0]))
        x = counts.index.tolist()
        y = counts.values
        y_norm = np.round((counts_y / counts.sum()) * 100,0)

        return {
            'series': counts,
            'x': counts_x,
            'y': counts_y,
            'y_norm': counts_y_norm
        }
    

