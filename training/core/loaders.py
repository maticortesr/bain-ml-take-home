"""Implementation of different data loaders.
CSVLoader is implemented, other loaders can be added later, 
like JSONLoader or RedshiftLoader.
"""

from core.base import DataLoader
import pandas as pd

class CSVLoader(DataLoader):
    def __init__(self, train_filepath=None, test_filepath=None):
        self.train_filepath = train_filepath
        self.test_filepath = test_filepath

    def run(self):
        """Load data from CSV files."""
        if self.train_filepath is None or self.test_filepath is None:
            raise ValueError("Both train and test file paths must be provided.")
        train_data = pd.read_csv(self.train_filepath)
        test_data = pd.read_csv(self.test_filepath)
        return train_data, test_data