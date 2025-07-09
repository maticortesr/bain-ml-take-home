from fastapi import APIRouter, Depends

from typing import Dict, Union
from models import PredictRequest, PredictResponse, ErrorResponse
from utils import ModelManager, validate_api_key
from config import Settings
from loguru import logger
import time
import uuid

router = APIRouter()
SETTINGS = Settings()
model_manager = ModelManager(model_path=SETTINGS.model_path)


@router.get("/")
async def home() -> Dict[str, str]:
    """Home endpoint to check if the API is running."""
    return {"message": "Bain Take Home API is running!"}


@router.post("/predict")
async def predict(
    input_data: PredictRequest, api_key: str = Depends(validate_api_key)
) -> Union[PredictResponse, ErrorResponse]:
    """Predict endpoint for making predictions using the loaded model.

    Args:
        input_data (PredictRequest): Input data for prediction, including model features and version.
        api_key (str, optional): API key for authentication.

    Returns:
        Union[PredictResponse, ErrorResponse]: Response containing the prediction result or an error message.
    """
    try:
        start = time.time()
        prediction_id = str(
            uuid.uuid4()
        )  # this can be persiste in a database for tracking

        logger.info(f"{prediction_id} INPUT: {input_data}")

        input_feature = input_data.model_features

        prediction = model_manager.predict(input_feature)
        prediction = int(prediction)  # Train and test data are integers

        logger.info(f"{prediction_id} PREDICTION: {prediction}")

        # Create a response object
        response = PredictResponse(
            status="success",
            model_version=input_data.model_version,
            prediction_label=SETTINGS.target_column,
            prediction_value=prediction,
        )
        end = time.time()
        logger.info(f"{prediction_id} TIMING: {end - start:.2f} seconds")
        return response
    except Exception as e:
        logger.error(f"ERROR: {e}")
        return ErrorResponse(
            status="error",
            message="An error occurred during prediction. Please check the input data and try again.",
        )
