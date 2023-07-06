import re
from datetime import date, datetime

from dateutil import relativedelta

months = {
    "Jan": "January",
    "Feb": "February",
    "March": "March",
    "April": "April",
    "May": "May",
    "June": "June",
    "July": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


def adjust_month(name):
    return months[name]


def date_validator(incomming_date, filter):
    # in case filter == 0
    filter = 1 if not filter else int(filter)
    if incomming_date[0].isdigit():
        incomming_date = date.today()

    # Adjust date_format
    for_upload = True
    commas = incomming_date.find(",")
    dot = incomming_date.find(".")
    if dot < 0:
        dot = incomming_date.find(" ")

    str_month = adjust_month(incomming_date[:dot].strip(" "))

    year = incomming_date[-4:] if commas > 0 else date.today().year
    month = str(datetime.strptime(str_month, "%B").month).zfill(2)
    day = str(incomming_date[dot : commas if commas > 0 else None]).zfill(2)

    # Make data notations and compare
    date_notation = datetime.strptime(f"{month}/{year}", "%m/%Y")
    month_today = str(date.today().month).zfill(2)
    year_today = str(date.today().year).zfill(2)
    today = datetime.strptime(f"{month_today}/{year_today}", "%m/%Y")

    delta = relativedelta.relativedelta(today, date_notation)

    if delta.months > filter:
        for_upload = False

    return for_upload, f"{day}/{month}/{year}"


def money_validator(title, description):
    pattern = r"\$\d+(\.\d+)?|\d+(\.\d+)? dollars?|\d+ USD"
    matches_title = re.findall(pattern, title)
    matches_desc = re.findall(pattern, description)

    if matches_desc or matches_title:
        return True
    return False
