from src.logger import logger
from src.utilities.dataframe_reader import DataFrameReader
from src.engine_constants import INPUT_PATH, INPUT_FIELD_NAMES
from src.data_cleaner import DataFrameCleaner
from src.model_pre_processor import ModelPreProcessor
from src.model_trainer import ModelTrainer

LOGGER = logger()

def main():
    LOGGER.info('****Enter Main****')

    data_reader = DataFrameReader(INPUT_PATH, INPUT_FIELD_NAMES)
    pandas_df = data_reader.get_pd_dataframe()

    data_cleaner = DataFrameCleaner(pandas_df)
    cleaned_df = data_cleaner.clean_dataframe()

    pre_processor = ModelPreProcessor(cleaned_df)
    x_train, x_test, y_train, y_test = pre_processor.pre_process_model()

    model_trainer = ModelTrainer(x_train, y_train, x_test, y_test)
    scores = model_trainer.train_and_score_model()

    print(scores)


if __name__ == "__main__":
    main()