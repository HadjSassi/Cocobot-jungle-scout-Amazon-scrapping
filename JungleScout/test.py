import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/home/keranis/.config/google-chrome/Default")
    options.add_argument("--load-extension=/home/keranis/.config/google-chrome/Default/Extensions/bckjlihkmgolmgkchbpiponapgjenaoa/7.4.0_0")
    # options.add_argument("--user-data-dir=C:\\Users\\mahdi\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    # options.add_argument("--load-extension=C:\\Users\\mahdi\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\bckjlihkmgolmgkchbpiponapgjenaoa\\7.4.0_0")
    browser = uc.Chrome(options=options)
    browser.get("https://www.google.com")
    browser.maximize_window()
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    input("press enter")
