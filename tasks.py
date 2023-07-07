from loguru import logger

from src.helpers.save_data import append_data_to_excel
from src.views.nyt_view import NYTView


def start_extraction():
    print("################")
    logger.info("Starting effective-octo-broccoli...")
    raw_data = NYTView().run()
    append_data_to_excel(raw_data)
    print("################")


if __name__ == "__main__":
    start_extraction()
