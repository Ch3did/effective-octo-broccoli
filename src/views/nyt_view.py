import time

from loguru import logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.helpers.get_env import MONTHS, NYT_URL, PHRASE, PICTURE_PATH, SECTION
from src.helpers.validator import date_validator, money_validator
from src.helpers.xpath import XpathNotations


class NYTView:
    def __init__(self) -> None:
        url = f"{NYT_URL}"
        self.driver = webdriver.Chrome()
        self.xpath = XpathNotations()

        # Start ChromeDrive
        self.driver.get(url)

        # Set window size
        self.driver.maximize_window()

    def select_date_range(self) -> None:
        "Select a year range news for filter results"

        # Removed cookie windown
        self.driver.find_element(By.XPATH, self.xpath.get_cookie_btn()).click()
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

        self.driver.find_element(By.XPATH, self.xpath.get_search_btn()).click()
        search_lable = self.driver.find_element(By.XPATH, self.xpath.get_search_field())
        search_lable.send_keys(f"{phrase}")
        search_lable.send_keys(Keys.ENTER)
        time.sleep(1)

    def adjust_sort(self) -> None:
        "Set sort by Newest"
        self.driver.find_element(By.XPATH, self.xpath.get_sort()).click()

    def get_data(self) -> dict:
        has_finish = False
        item = 1
        error = 0
        data = []
        while not has_finish:
            time.sleep(1)
            logger.info(f"Running item {item}")
            page_len = len(
                self.driver.find_elements(By.XPATH, self.xpath.get_all_in_page())
            )

            try:
                date = self.driver.find_element(
                    By.XPATH, self.xpath.get_date(item)
                ).text

                date_response = date_validator(date, int(MONTHS))
                date = date_response[1]

                if date_response[0]:
                    logger.info("Find new info")
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
                        "picture_path": f"{PICTURE_PATH}{self.driver.find_element(By.XPATH, self.xpath.get_title(item)).text}.png",
                    }

                    news["has_money_on_it"] = (
                        True
                        if money_validator(news["title"], news["description"])
                        else False
                    )

                    filename = news["title"].lower().replace(" ", "")
                    with open(f"{PICTURE_PATH}/{filename}.png", "wb") as file:
                        file.write(
                            self.driver.find_element(
                                By.XPATH, self.xpath.get_picture_name(item)
                            ).screenshot_as_png
                        )

                    data.append(news)

                else:
                    logger.info(f"Finish extraction! Find {item-error} posts")
                    has_finish = True

                item += 1

            except NoSuchElementException as er:
                logger.error(f"Unable to find post on item {item}")
                item += 1
                error = 1

            if item > page_len:
                logger.info("Open more itens")
                self.driver.find_element(By.XPATH, self.xpath.btn_show_more()).click()

        return data

    def run(self) -> dict:
        # Added filters
        self.uses_search()
        self.select_date_range()
        self.select_section()
        self.adjust_sort()

        return self.get_data()
