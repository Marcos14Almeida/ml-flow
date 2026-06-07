
from ml_flow_mrc.core.ml_flow_test import predict_new_data
from ml_flow_mrc.utils.logger import app_log


def main() -> None:
    """Run the main entry point."""

    app_log.header("MLflow Start!")

    predict_new_data()


if __name__ == "__main__":
    main()
