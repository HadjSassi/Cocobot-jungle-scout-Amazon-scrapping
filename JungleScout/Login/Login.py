import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import JungleScout.Login.constants as const
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image

options = webdriver.ChromeOptions()
options.add_extension('/home/keranis/work&study/Cocobot-jungle-scout-Amazon-scrapping/JungleScout/Login/js.crx')
options.add_argument('--user-data-dir=/home/keranis/.config/google-chrome/Default')
class Login(uc.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super().__init__(options=options)
        # self.implicitly_wait(100)
        self.maximize_window()
        self.collection = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        else:
            input('Press Any key to close the program and press enter')

    def land_first_page(self):
        self.implicitly_wait(50)
        pass
        # self.get(const.jungle)
        # self.implicitly_wait(100)
        # time.sleep(5)
        # email = self.find_element(
        #     By.ID, "email"
        # )
        # email.clear()
        # email.send_keys("anisse9@gmail.com")
        # pswd = self.find_element(
        #     By.ID, "current-password"
        # )
        # pswd.clear()
        # pswd.send_keys("million10")

        # time.sleep(5)
        # self.find_element(
        #     By.CLASS_NAME, "ButtonWrapper-sc-1qb4ldc-0"
        # ).click()
        # self.get(const.google)
        # option = webdriver.ChromeOptions
        # option.add_extension("")