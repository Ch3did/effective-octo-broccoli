from openpyxl import load_workbook

from src.helpers.get_env import FILE_NAME


def append_data_to_excel(data):
    file_path = f"tmp/{FILE_NAME}.xml"

    # Load the existing workbook
    workbook = load_workbook(file_path)

    # Access the active sheet
    sheet = workbook.active

    # Get the data columns from the request body dictionary
    columns = list(data.keys())

    # Append the data to the next available row in the sheet
    new_row = [data[column] for column in columns]
    sheet.append(new_row)

    # Save the updated workbook
    workbook.save(file_path)

    # Close the workbook
    workbook.close()
