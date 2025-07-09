    

from fastapi.security import APIKeyHeader
from fastapi import Depends, HTTPException
from config import Settings
import joblib
import pandas as pd

class ModelManager:
    """Loads model from path using joblib."""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = self.load()

    def load(self):
        """Load the model from the specified path."""
        return joblib.load(self.model_path)
    
    def predict(self, features: dict) -> float:
        """Predict using the loaded model."""
        features_df = pd.DataFrame([features.model_dump()])
        prediction = self.model.predict(features_df)

        return float(prediction[0]) if len(prediction) > 0 else None


api_key_header = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != Settings().api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key