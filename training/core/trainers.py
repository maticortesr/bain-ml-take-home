"""Implementation of different model trainers.
SKLearnTrainer is implemented, Pytorch and TensorFlow can be added later.

"""

from sklearn.base import BaseEstimator
from core.base import ModelTrainer
from sklearn.pipeline import Pipeline


class SKLearnTrainer(ModelTrainer):
    def __init__(self, model: BaseEstimator, transformer=None):
        self.model = model
        self.transformer = transformer

    def _build_pipeline(self):
        """Build a pipeline with the transformer if provided."""
        if self.transformer is not None:
            return Pipeline(steps=[('transformer', self.transformer), ('model', self.model)])
        else:
            return self.model

    def run(self, data):
        X, y = data
        pipeline = self._build_pipeline()

        pipeline.fit(X, y)
        return pipeline