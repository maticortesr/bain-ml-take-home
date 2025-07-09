from abc import ABC, abstractmethod

class PipelineStep(ABC):
    @abstractmethod
    def run(self, data):
        """Run the step on the given data and return the result."""
        pass

class DataLoader(PipelineStep):
    @abstractmethod
    def run(self, data=None):
        """Load and return the initial dataset."""
        pass

class ModelTrainer(PipelineStep):
    @abstractmethod
    def run(self, data):
        """Train the model and return the trained model."""
        pass

class ModelEvaluator(PipelineStep):
    @abstractmethod
    def run(self, model, data):
        """Evaluate the model and return evaluation metrics."""
        pass
