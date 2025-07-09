from pydantic_settings import BaseSettings
from pydantic import Field, BaseModel

class Hyperparameters(BaseModel):
    """
    Hyperparameters for the model.
    """
    learning_rate: float = Field(
        0.01,
        description="Learning rate for the model."
    )
    n_estimators: int = Field(
        300,
        description="Number of boosting stages to be run."
    )
    max_depth: int = Field(
        5,
        description="Maximum depth of the individual regression estimators."
    )
    loss: str = Field(
        'absolute_error',
        description="Loss function to be optimized."
    )

class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """
    target_column: str = Field(
        "price",
        description="The name of the target column in the dataset."
    )
    categorical_columns: list[str] = Field(
        ["type", "sector"],
        description="List of categorical columns in the dataset."
    )
    training_data_path: str = Field(
        "data/train.csv",
        description="Path to the training data CSV file."
    )
    test_data_path: str = Field(
        "data/test.csv",
        description="Path to the test data CSV file."
    )
    model_output_path: str = Field(
        "output/model.pkl",
        description="Path to save the trained model."
    )
    hyperparameters: Hyperparameters = Hyperparameters()

    metrics: list[str] = Field(
        ["mae", "rmse","mape"],
        description="List of metrics to evaluate the model."
    )

