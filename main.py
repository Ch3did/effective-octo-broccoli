from src.helpers.save import append_data_to_excel
from src.views.nyt_view import NYTView


def start_extraction():
    raw_data = NYTView().run()
    append_data_to_excel(raw_data)


if __name__ == "__main__":
    start_extraction()


# import re

# string = "Here are some examples: $11.1, $111,111.11, 11 dollars, 11 USD"

# pattern = r"\$\d+(\.\d+)?|\d+(\.\d+)? dollars?|\d+ USD"

# matches = re.findall(pattern, string)

# for match in matches:
#     print(match)
