from src.logger import logger
from src.utilities.dataframe_reader import DataFrameReader
from src.engine_constants import INPUT_PATH, INPUT_FIELD_NAMES

def main():
    # for loop to run all workflows for one or more search queries
    # LOGGER = logger()
    # LOGGER.info('********** Entering main() ******BEGIN******\n')

    data_reader = DataFrameReader(INPUT_PATH, INPUT_FIELD_NAMES)
    pandas_df = data_reader.get_pd_dataframe()

    print(pandas_df.head())


if __name__ == "__main__":
    main()