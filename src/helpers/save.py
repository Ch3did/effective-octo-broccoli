import pandas as pd

from src.helpers.get_env import FILE_NAME


def append_data_to_excel(data_list):
    file_path = f"tmp/{FILE_NAME}.xlsx"

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Create an Excel writer using pandas
    writer = pd.ExcelWriter(file_path, engine="xlsxwriter")

    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False, sheet_name="Sheet1")

    # Save the Excel file
    writer.close()
