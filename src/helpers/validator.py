from datetime import datetime, date
from dateutil import relativedelta
import re


def date_validator(incomming_date, filter):
    # in case filter == 0
    filter = 1 if not filter else int(filter)
    if incomming_date[0].isdigit():
        incomming_date = date.today()

    # Adjust date_format
    for_upload = True
    commas = incomming_date.find(',')
    dot = incomming_date.find('.')
    str_month = incomming_date[:dot].strip(" ")

    year = incomming_date[-4:] if  commas else date.today().year
    month = str(datetime.strptime(str_month, "%B").month)
    day = incomming_date[dot: commas if commas>0 else None]
    
    # Make data notations and compare
    date_notation = datetime.strptime(f"{month}/{year}", "%m/%Y")
    today = datetime.strptime(f'{date.today().month}/{date.today().year}', "%m/%Y")

    delta = relativedelta.relativedelta(date_notation, today)

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