import unittest

import numpy as np
from src.utilities.data_imputer import DataImputer

class TestDataImputer(unittest.TestCase):

    def test_data_imputer(self):
        
        test_array = np.array([76.6, 77.7, 72.9, 77.9 , np.nan])
        test_array = test_array.reshape(-1, 1)

        imputer = DataImputer()
        imputed_array = imputer.impute_w_knn(test_array)

        self.assertEqual(([[76.275]]), imputed_array[-1])