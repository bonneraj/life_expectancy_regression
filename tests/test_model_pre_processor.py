import unittest
import pandas as pd
import numpy as np
from src.model_pre_processor import ModelPreProcessor

class TestModelPreProcessor(unittest.TestCase):

    def test_create_feature_label_arrays(self):
        column_names = ['test_label', 'test_feature']
        data = [['a', 1],['b', 2], ['c', 3], ['a', 1],['b', 2], ['c', 3], ['c', 3],['b', 2], ['c', 3], ['c', 3]] 
        df = pd.DataFrame(data=data, columns=column_names)
        
        pre_processor = ModelPreProcessor(df)
        label_array, feature_array = pre_processor._create_feature_label_arrays(feature_cols=['test_feature'], label_col=['test_label'])

        self.assertEqual(10, len(feature_array))
        self.assertEqual(10, len(label_array))

    def test_create_test_train_split(self):
        column_names = ['test_label', 'test_feature']
        data = [['a', 1],['b', 2], ['c', 3], ['a', 1],['b', 2], ['c', 3], ['c', 3],['b', 2], ['c', 3], ['c', 3]] 
        df = pd.DataFrame(data=data, columns=column_names)
        
        pre_processor = ModelPreProcessor(df)
        label_array, feature_array = pre_processor._create_feature_label_arrays(feature_cols=['test_feature'], label_col=['test_label'])

        x_train, x_test, y_train, y_test = pre_processor._create_train_test_split(label_array, feature_array, test_size=.3, random_state=42)
    
        self.assertEqual(7, len(x_train))
        self.assertEqual(np.array(1), x_train[0])

        self.assertEqual(3, len(x_test))
        self.assertEqual(np.array(3), x_test[0])
        
        self.assertEqual(7, len(y_train))
        self.assertEqual(np.array('a'), y_train[0])
        
        self.assertEqual(3, len(y_test))
        self.assertEqual(np.array('c'), y_test[0])
