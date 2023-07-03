import time

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.helpers.get_env import NYT_URL, PHRASE, SECTION
from src.helpers.xpath import XpathNotations


class NYTView:
    def __init__(self) -> None:
        url = f"{NYT_URL}"
        self.driver = webdriver.Chrome()
        self.xpath = XpathNotations()

        # Start ChromeDrive
        self.driver.get(url)

        # Set window size
        self.driver.set_window_size(1240, 981)
        self.driver.maximize_window()

    def select_date_range(self) -> None:
        "Select a year range news for filter results"
        date_btn = self.driver.find_element(By.XPATH, self.xpath.get_date_btn())
        date_btn.click()

        a_year = self.driver.find_element(By.XPATH, self.xpath.get_btn_year())
        a_year.click()

        time.sleep(1)
        date_btn.click()

    def select_section(self) -> None:
        "Uses section varible to filter results"
        section_btn = self.driver.find_element(By.XPATH, self.xpath.get_btn_section())
        section_btn.click()

        section_list = self.driver.find_elements(
            By.XPATH, self.xpath.get_section_list()
        )

        sections_name = [item.text for item in section_list]

        section = SECTION.title()

        if section in sections_name:
            index = sections_name.index(section)
            selected_section = self.driver.find_element(
                By.XPATH, self.xpath.get_section(index + 1)
            )
            time.sleep(1)
            selected_section.click()

        else:
            logger.error(f"Category {section} Not Found!!!")

        section_btn.click()

    def uses_search(self):
        phrase = PHRASE.lower()

        search_filed = self.driver.find_element(By.XPATH, self.xpath.get_search_field())
        search_filed.send_keys(f"{phrase}")

        search_btn = self.driver.find_element(By.XPATH, self.xpath.get_search_btn())
        search_btn.click()

    def run(self) -> dict:
        data_dict = {}

        # Added filters
        self.select_date_range()
        self.select_section()
        self.uses_search()

        data = self.extract_data()

        for item in data:
            item.append(data_dict)

        return data_dict
