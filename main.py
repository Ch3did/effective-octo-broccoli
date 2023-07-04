from src.helpers.save import append_data_to_excel
from src.views.nyt_view import NYTView


def start_extraction():
    raw_data = NYTView().run()
    append_data_to_excel(raw_data)


if __name__ == "__main__":
    start_extraction()
