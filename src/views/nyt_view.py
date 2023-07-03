import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.helpers.get_env import NYT_URL


class NYTView:
    def __init__(self) -> None:
        self.url = f"{NYT_URL}"
        self.driver = webdriver.Chrome()

        
    def run(self) -> dict:
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.set_window_size(1240, 981)
        value = self.driver.find_elements(By.XPATH, "")

        
        data_dict = {}
        return data_dict