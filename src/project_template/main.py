from project_template.core.business_logic import hello_world
from project_template.utils.logger import logg


if __name__ == "__main__":
    logg.info(hello_world())
