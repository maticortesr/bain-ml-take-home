from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """
    model_config = SettingsConfigDict(env_prefix='BAIN_')
    target_column: str = Field(
        "price",
        description="The name of the target column in the dataset."
    )
    model_path: str = Field(
        "./artifacts/model.pkl",
        description="Path to load the trained model."
    )
    api_key: str = ''
