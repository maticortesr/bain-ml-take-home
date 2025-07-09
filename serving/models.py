from pydantic import BaseModel
from typing import Union


class ModelFeatures(BaseModel):
    type: str
    sector: str
    net_usable_area: float
    net_area: float
    n_rooms: float
    n_bathroom: float
    latitude: float
    longitude: float


class PredictRequest(BaseModel):
    model_version: str
    model_features: ModelFeatures

class PredictResponse(BaseModel):
    status: str
    model_version: str
    prediction_label: str
    prediction_value: Union[int,None] = None # Prediction can be None if an error occurs

class ErrorResponse(BaseModel):
    status: str
    message: str