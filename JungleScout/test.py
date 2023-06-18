import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument(r'--user-data-dir=/home/keranis/.config/google-chrome/Default')
    options.add_extension('/home/keranis/work&study/Cocobot-jungle-scout-Amazon-scrapping/JungleScout/Login/js.crx')
    browser = uc.Chrome(options=options)
    browser.get("https://members.junglescout.com/#/database")
    input("press enter")