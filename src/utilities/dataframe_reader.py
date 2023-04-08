from src.logger import logger
import pandas as pd

LOGGER = logger()

class DataFrameReader:

    def __init__(self, file_path: str, column_names: list):
        self.file_path = file_path
        self.column_names = column_names

    def get_pd_dataframe(self):
        LOGGER.info(f'Retrieving file from {self.file_path}')
        dataframe = pd.read_csv(self.file_path, names=self.column_names, header=0)
        return dataframe