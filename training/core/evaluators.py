from core.base import ModelEvaluator
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
import numpy as np


AVAILABLE_SKLEARN_METRICS = {
    'rmse': lambda y_true, y_pred: np.sqrt(mean_squared_error(y_true, y_pred)),
    'mape': mean_absolute_percentage_error,
    'mae': mean_absolute_error,
}


class SKLearnEvaluator(ModelEvaluator):
    def __init__(self, metrics=['mae']):
        self.metrics = metrics
        self.results = {}

    def run(self, model, data):
        X, y = data
        y_pred = model.predict(X)
        for metric in self.metrics:
            if metric in AVAILABLE_SKLEARN_METRICS:
                score = AVAILABLE_SKLEARN_METRICS[metric](y, y_pred)
                self.results[metric] = float(score)
            else:
                raise ValueError(f"Metric '{metric}' is not available. Choose from {list(AVAILABLE_SKLEARN_METRICS.keys())}.")
