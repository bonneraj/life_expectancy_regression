import unittest
import pandas as pd
import numpy as np
from src.data_cleaner import DataFrameCleaner

class TestDataFrameReader(unittest.TestCase):       
    
    # test final output after all cleaning
    def test_dataframe_cleaner(self):
        column_names = ['fips', 'state', 'county', 'measure_1', 'measure_2', 'majority_null_measure', 'age_adj_suicide_rate', 'age_adj_death_rate', 'percent_frequent_physical_distress', 'percent_frequent_mental_distress']
        data = [['1', 'Virginia', np.nan, 100, 12, 2, '1', '1', '1', '1'],['2', 'Virginia', 'Fairfax', 20, 42, np.nan, '1', '1', '1', '1'], ['3', 'Virginia', 'Arlington', 20, 42, np.nan, '1', '1', '1', '1']] 
        df = pd.DataFrame(data=data, columns=column_names)
        
        cleaner = DataFrameCleaner(df)
        result_df = cleaner.clean_dataframe() 

        self.assertEqual(2, len(result_df)) # 2 resulting rows
        self.assertEqual(2, result_df.shape[1]) # 2 resulting columns