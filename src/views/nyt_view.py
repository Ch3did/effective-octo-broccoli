import time

from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from helpers.validator import date_validator, money_validator
from src.helpers.get_env import MONTHS, NYT_URL, PHRASE, SECTION
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

        # Removed cookie windown
        self.driver.find_element(By.XPATH, self.xpath.get_cookie_btn()).click()

    def select_date_range(self) -> None:
        "Select a year range news for filter results"

        logger.info("Starting filtering using Date")
        date_btn = self.driver.find_element(By.XPATH, self.xpath.get_date_btn())
        date_btn.click()

        a_year = self.driver.find_element(By.XPATH, self.xpath.get_btn_year())
        a_year.click()

        time.sleep(1)
        date_btn.click()

    def select_section(self) -> None:
        "Uses section varible to filter results"

        section = SECTION.title()

        logger.info(f"Starting filtering using section '{section}'")
        section_btn = self.driver.find_element(By.XPATH, self.xpath.get_btn_section())
        section_btn.click()

        section_list = self.driver.find_elements(
            By.XPATH, self.xpath.get_section_list()
        )

        # Get sanatized sections name
        sections_name = []
        for item in section_list:
            result = "".join([i for i in item.text if not i.isdigit() and i != ","])
            sections_name.append(result)

        # find section
        if section in sections_name:
            index = sections_name.index(section)
            selected_section = self.driver.find_element(
                By.XPATH, self.xpath.get_section(index + 1)
            )
            selected_section.click()

        else:
            logger.error(f"Category '{section}' Not Found!!!")

        time.sleep(1)
        section_btn.click()

    def uses_search(self) -> None:
        "Inpput the key phrase and start search"
        phrase = PHRASE.lower()

        logger.info(f"Starting filtering using phrase '{phrase}'")

        search_filed = self.driver.find_element(By.XPATH, self.xpath.get_search_field())
        search_filed.send_keys(f"{phrase}")

        search_filed.send_keys(Keys.ENTER)
        time.sleep(1)

    def get_data(self) -> dict:
        has_finish = False
        item = 1
        data = []
        while not has_finish:
            page_len = len(
                self.driver.find_elements(By.XPATH, self.xpath.get_date(item))
            )

            try:
                date = self.driver.find_element(
                    By.XPATH, self.xpath.get_date(item)
                ).text

                date_response = date_validator(date, MONTHS)
                date = date_response[1]

                if date_response[0]:
                    news = {
                        "date": date,
                        "title": self.driver.find_element(
                            By.XPATH, self.xpath.get_title(item)
                        ).text,
                        "description": self.driver.find_element(
                            By.XPATH, self.xpath.get_description(item)
                        ).text,
                        "picture_url": self.driver.find_element(
                            By.XPATH, self.xpath.get_picture_name(item)
                        ).get_attribute("src"),
                        "picture_path": f"tmp/{self.driver.find_element(By.XPATH, self.xpath.get_title(item)).text}.png",
                    }

                    news["has_money_on_it"] = (
                        True
                        if money_validator(news["title"], news["description"])
                        else False
                    )

                    filename = news["title"].lower().replace(" ", "")
                    with open(f"tmp/{filename}.png", "wb") as file:
                        file.write(
                            self.driver.find_element(
                                By.XPATH,
                                self.xpath.get_picture_name(item).screenshot_as_png,
                            )
                        )

                    data.append(news)

                else:
                    has_finish = True

                item += 1

            except NoSuchElementException as error:
                logger.error("Unable to find Element")
                has_finish = True

            if item > page_len:
                self.driver.find_elements(By.XPATH, self.xpath.get_date(item)).click()

        return data

    def run(self) -> dict:
        data_dict = {}

        # Added filters
        self.select_date_range()
        self.select_section()
        self.uses_search()

        return self.get_data()
