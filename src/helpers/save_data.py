import pandas as pd
from loguru import logger

from src.helpers.get_env import FILE_NAME, MONTHS, PHRASE


def append_data_to_excel(data_list):
    file_path = f"tmp/{FILE_NAME}_{MONTHS}-months_{PHRASE}.xlsx"

    df = pd.DataFrame(data_list)
    writer = pd.ExcelWriter(file_path, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name="Sheet1")

    # Save the Excel file
    logger.info(f"Creating file {file_path[4:]}")
    writer.close()
