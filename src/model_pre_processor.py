from src.engine_constants import FEATURE_FIELDS, LABEL_FIELD, TEST_SIZE, RANDOM_STATE
import numpy as np
from src.utilities.data_imputer import DataImputer
from sklearn.model_selection import train_test_split

class ModelPreProcessor:
    '''A class to pre-process a pandas dataframe for model training. 
    Includes creating array from pandas df, imputing missing data, splitting features/label
    
    Returns test/train split arrays for model ingestion.'''
    
    def __init__(self, dataframe):
        self.df = dataframe
    
    def pre_process_model(self):
                
        self.label_array, self.feature_array = self._create_feature_label_arrays(FEATURE_FIELDS, LABEL_FIELD)

        imputer = DataImputer()
        label_array = imputer.impute_w_knn(self.label_array)
        feature_array = imputer.impute_w_knn(self.feature_array)

        self.x_train, self.x_test, self.y_train, self.y_test = self._create_train_test_split(feature_array, label_array, TEST_SIZE, RANDOM_STATE)

        return self.x_train, self.x_test, self.y_train, self.y_test

    def _create_feature_label_arrays(self, feature_cols: list, label_col: list):
        label_array = np.array(self.df[label_col])
        feature_array = np.array(self.df[feature_cols])

        return label_array, feature_array

    def _create_train_test_split(self, label_array, feature_array, test_size, random_state):
        return train_test_split(feature_array, label_array, test_size=test_size, random_state=random_state)