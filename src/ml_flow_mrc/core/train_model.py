import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from ml_flow_mrc.utils.logger import app_log


def train_and_log() -> None:
    """
    Train the model and log the results.

    This function runs the training process and records relevant
    metrics or messages using the configured app_log.
    """

    # Load dataset
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Log with MLflow
    with mlflow.start_run():
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, name="model", serialization_format="skops")

    app_log.info(f"Model trained and app_loged with accuracy: {acc:.2f}")
