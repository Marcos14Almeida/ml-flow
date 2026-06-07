
from ml_flow_mrc.core.ml_flow_test import predict_new_data
from ml_flow_mrc.utils.logger import logg


def main() -> None:
    """Run the main entry point."""
    logg.header("MLflow Start!")

    predict_new_data()


if __name__ == "__main__":
    main()
