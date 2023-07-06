from loguru import logger

from src.helpers.save_data import append_data_to_excel
from src.views.nyt_view import NYTView


def start_extraction():
    print("################")
    raw_data = NYTView().run()
    append_data_to_excel(raw_data)
    logger.info("Finish Task")
    print("################")


if __name__ == "__main__":
    start_extraction()
