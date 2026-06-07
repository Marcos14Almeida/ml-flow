import mlflow
import numpy as np


def predict_new_data() -> None:
    """
    Predict new data using the latest MLflow model.

    Loads the most recent model from MLflow, applies it to a sample
    dataset (Iris features in this example), and prints the prediction
    result to the console.
    """

    # Load the latest model from MLflow
    model_uri = "runs:/<RUN_ID>/model"  # Replace <RUN_ID> with the run ID from MLflow UI
    model = mlflow.sklearn.load_model(model_uri)

    # Example new data (Iris features)
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(sample)

    print(f"Prediction for {sample}: {prediction}")
