import time

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.helpers.get_env import NYT_URL, SECTION
from src.helpers.xpath import XpathNotations


class NYTView:
    def __init__(self) -> None:
        self.url = f"{NYT_URL}"
        self.driver = webdriver.Chrome()
        self.xpath = XpathNotations()

    def select_section(self):
        categories = self.driver.find_elements(By.XPATH, self.xpath.get_categories())

        categories_name = [item.text for item in categories]
        section = SECTION.title()

        if section in categories_name:
            index = categories_name.index(section)
            el = self.driver.find_element(
                By.XPATH, self.xpath.get_category_element(index)
            )
            el.click()

        else:
            logger.error(f"Category {section} Not Found!!!")

    def extract_data(self):
        pass

    def run(self) -> dict:
        data_dict = {}
        self.driver.get(self.url)
        self.driver.set_window_size(1240, 981)
        self.driver.maximize_window()

        self.select_section()

        data = self.extract_data()

        for item in data:
            item.append(data_dict)

        return data_dict
