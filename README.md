# Bain ML Challenge

This repository contains the solution for the Bain ML Challenge, which involves building a machine learning model to predict the price of properties based on various features. The solution includes a training pipeline, an API for serving predictions, and a Docker setup for deployment.

### Project Structure

Training Pipeline:
- `training/`: Contains the code for training the machine learning model.
    - `core/`: Contains the base classes and utilities for the training pipeline.
    - `config.py`: Configuration settings for the training pipeline.
    - `data/`: Contains the dataset used for training and testing the model (not included in the repository).
    - `Dockerfile`: Dockerfile for building the training pipeline image.
    - `main.py`: Main script for running the training pipeline.
- `serving/`: Contains the code for serving the trained model via an API.
    - `models/`: Contains the schema classes and utilities for serving predictions.
    - `config.py`: Configuration settings for the API server.
    - `routes.py`: Defines the API endpoints and request handling logic.
    - `Dockerfile`: Dockerfile for building the API server image.
    - `app.py`: Main script for running the API server.
    - `.env`: Environment variables for the API server (API key, etc.).

### How to Run

1. Run training pipeline first to train the model and save it to a file, check details in [training/README.md](training/README.md).
2. Run the API server to serve predictions, check details in [serving/README.md](serving/README.md).



### Model Improvement notes:

* Price variable being used to train model, corrected in training pipeline.
* No hyperparameter tuning, GridSearch was imported but not used.
* No feature engineering, only using the features provided in the dataset.
* No data preprocessing, no handling of missing values or categorical variables.
* Missed opportunity to use the geospatial data provided.
* No cross-validation, only train-test split.
* No model monitoring, no logging or tracking of model performance.
* Notebook failed with recent Scikit-learn library, downgraded to version 1.5.2.

### Implementation improvements:

Some things not implemented but would be good to have in the future:
* Route versioning
* Add ML experiment tracker like MLflow
* Use ONNX for model serialization when serving
* This implementation only handles 1 user with 1 API key, a more sofisticated system would handle multiple users and their keys.
* Model is persisted locally, a more robust solution would involve S3 or other remote storage solution.
* Cache can be added to API to improve performace for repeated requests.
* CICD, Pre-commit hooks, and other DevOps practices can be added to improve the development process.
