import joblib
import os

from core.loaders import CSVLoader
from core.trainers import SKLearnTrainer
from core.evaluators import SKLearnEvaluator
from config import Settings

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from category_encoders import TargetEncoder

SETTINGS = Settings()


def main():
    # Load data
    loader = CSVLoader(
        train_filepath=SETTINGS.training_data_path,
        test_filepath=SETTINGS.test_data_path,
    )
    train, test = loader.run()

    # Preprocess data
    target = SETTINGS.target_column
    train_cols = [col for col in train.columns if col not in ["id", target]]
    categorical_cols = SETTINGS.categorical_columns
    categorical_transformer = TargetEncoder()

    processor = ColumnTransformer(
        transformers=[("categorical", categorical_transformer, categorical_cols)]
    )

    # Train model
    hyperparameters = SETTINGS.hyperparameters.model_dump(mode="json")
    model = GradientBoostingRegressor(**hyperparameters)
    
    trainer = SKLearnTrainer(model=model, transformer=processor)
    trained_model = trainer.run(data=(train[train_cols], train[target]))

    # Evaluate model
    evaluator = SKLearnEvaluator(metrics=SETTINGS.metrics)
    evaluator.run(model=trained_model, data=(test[train_cols], test[target]))

    # Print results
    print(evaluator.results)

    # Save the trained model

    os.makedirs(os.path.dirname(SETTINGS.model_output_path), exist_ok=True)
    joblib.dump(trained_model, SETTINGS.model_output_path)
    
    print(f"Model saved to {SETTINGS.model_output_path}")


if __name__ == "__main__":
    main()
