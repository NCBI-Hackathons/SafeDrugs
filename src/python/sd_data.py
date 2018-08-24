
from pyarrow import feather
import numpy as np

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

    def count(self, query):
        return self.data.query(query).count().values[0]
            

    def counts_by_feature(self, feature, query=""):
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

        ds = self.data.query(query) if query else self.data
                  
        series = (ds.groupby([feature])
                  .apply(lambda x : x.shape[0]))
        x = series.index.tolist()
        y = series.values
        y_norm = np.round((y / series.sum()) * 100,0)

        return {
            'series': series,
            'x': x,
            'y': y,
            'y_norm': y_norm
        }
    

