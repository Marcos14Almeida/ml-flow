import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-5s | %(message)-70s | %(filename)s:%(lineno)d",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logg = logging.getLogger(__name__)
