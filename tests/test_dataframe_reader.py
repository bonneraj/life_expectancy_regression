import unittest

from src.utilities.dataframe_reader import DataFrameReader
from src.engine_constants import INPUT_PATH, INPUT_FIELD_NAMES

class TestDataFrameReader(unittest.TestCase):

    def test_dataframe_reader(self):
        data_reader = DataFrameReader(INPUT_PATH, INPUT_FIELD_NAMES)
        df = data_reader.get_pd_dataframe()
        
        self.assertEqual(3193, len(df))
        self.assertEqual(47, len(df.columns))
        self.assertEqual(['fips', 'state', 'county'], list(df.columns)[:3])