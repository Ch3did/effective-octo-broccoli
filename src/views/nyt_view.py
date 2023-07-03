import time

from selenium import webdriver

from src.helpers.get_env import NYT_URL


class NYTView:
    def __init__(self) -> None:
        self.url = f"{NYT_URL}"
        self.driver = webdriver.Firefox()

        
    def run(self) -> dict:
        self.driver.get(self.url)
        time.sleep(3)
        
        
        
        
        data_dict = {}
        return data_dict