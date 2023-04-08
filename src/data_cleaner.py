import pandas as pd
from src.engine_constants import ID_FIELDS, UNUSED_LABEL_FIELDS
import numpy as np

class DataFrameCleaner():

    def __init__(self, dataframe):
        self.df = dataframe

    def clean_dataframe(self):
        self.df = self._insert_np_nan()
        null_percentages_df = self._check_percent_null()
        columns_to_remove = self._get_null_columns_to_remove(null_percentages_df)
        self.df = self._remove_columns_from_df(columns_to_remove)
        self.df = self._remove_state_level_rows(self.df)
        self.df = self._remove_columns_from_df(ID_FIELDS)
        self.df = self._remove_columns_from_df(UNUSED_LABEL_FIELDS)

        return self.df

    def _insert_np_nan(self):
        return self.df.fillna(np.nan)

    def _check_percent_null(self):
        '''For a given column, find the percent of rows that are null.'''
        null_df_header_list = []
        null_df_value_list = []

        for col in self.df.columns.to_list():
            null_df = self.df[col]
            null_count = (null_df.isna().sum())
            null_percentage = (100*null_count)/len(null_df)
            null_df_header_list.append(col)
            null_df_value_list.append(round(null_percentage, 2))
            list_of_tuples = list(zip(null_df_header_list, null_df_value_list)) 

        return pd.DataFrame(list_of_tuples, columns=['column', 'null_percentage']).sort_values(by=['null_percentage'], ascending=False).set_index('column')

    def _get_null_columns_to_remove(self, dataframe, null_threshold=50):
        '''Given a dataframe of columns and percentage of rows with null values, identify the columns that have a percentage of nulls exceeding a specified threshold. 
        The default threshold is 50 (50%).'''
        over_null_threshold_df = dataframe.loc[dataframe['null_percentage'] > null_threshold]
        return over_null_threshold_df.index.to_list()

    def _remove_columns_from_df(self, columns_to_remove: list):
        '''Removes specified column(s) from a pandas dataframe'''
        return self.df.drop(columns=columns_to_remove)

    def _remove_state_level_rows(self, dataframe):
        '''Remove state-level measures and outcomes, leaving only county-level. State-level rows can be found where there are null values in the county column.'''
        return dataframe.dropna(subset=['county'])