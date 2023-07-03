import os

from dotenv import load_dotenv

load_dotenv(".env")

# Debug for loger
DEBUG = os.environ.get("DEBUG")

# Excel File Name
FILE_NAME = os.environ.get("FILE_NAME")

# category new's
SECTION =  os.environ.get("SECTION")

# URL Views
NYT_URL = os.environ.get("NEW_YOUR_TIMES")
