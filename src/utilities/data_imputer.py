from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer, IterativeImputer
import numpy as np

class DataImputer:

    def impute_w_knn(self, array):
        imputer = KNNImputer(n_neighbors=3, missing_values=np.nan)
        
        return imputer.fit_transform(array)

    # def impute_w_iteration():

    # def impute_w_mean():