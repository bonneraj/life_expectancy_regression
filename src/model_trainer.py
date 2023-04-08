from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class ModelTrainer:

    def __init__(self, x_train, y_train, x_test, y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test

    def train_and_score_model(self):
        model = self._train_model()
        predictions_array = self._get_predictions(model)
        scores_dict = self._get_model_scores(predictions_array)

        return scores_dict

    def _train_model(self):
        lr = LinearRegression()
        lr.fit(self.x_train, self.y_train)
        return lr

    def _get_predictions(self, trained_model):
        return trained_model.predict(self.x_test)

    def _get_model_scores(self, predictions_array):
        r2 = r2_score(self.y_test, predictions_array)

        mae = mean_absolute_error(self.y_test, predictions_array)

        mse = mean_squared_error(self.y_test, predictions_array)

        return {"R2": r2, "MAE": mae, "MSE": mse}
