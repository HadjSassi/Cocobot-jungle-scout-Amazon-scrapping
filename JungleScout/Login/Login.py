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
options.add_argument("--user-data-dir=/home/keranis/.config/google-chrome/Default")
options.add_argument("--load-extension=/home/keranis/.config/google-chrome/Default/Extensions/bckjlihkmgolmgkchbpiponapgjenaoa/7.4.0_0")
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
        # query = input("What would you search ?")
        query = "I phone 10"
        self.get(const.amazon + f"/s?k={query.replace(' ', '+')}")
        self.implicitly_wait(100)
        self.switch_to.window(self.window_handles[1])
        self.close()
        self.switch_to.window(self.window_handles[0])
        self.implicitly_wait(100)
        time.sleep(5)
        try :
            # jsBtn = WebDriverWait(self, 100).until(
            #     EC.presence_of_element_located((By.ID, "popup-button"))
            # )
            jsBtn = self.find_element(By.ID,"popup-button")
            jsBtn.click()
            time.sleep(5)
            stillRecherche = True
            while(stillRecherche):
                try:
                    jsBtn = self.find_element(By.CSS_SELECTOR,"#jsExtensionBaseModalId > div.Container-sc-1tzcbkm-1.gNfIMq > div > div.Flex-sc-sqmtka-0.TableContainer-sc-ybu0mp-1.bXUgal.hhoMvF > div.Flex-sc-sqmtka-0.Container-sc-n6pzpt-0.eQnaRt.huoEMs > div:nth-child(2) > div.Flex-sc-sqmtka-0.ftsCjc > button")
                    jsBtn.click()
                    time.sleep(5)
                    updatedContent = self.find_element(By.CSS_SELECTOR,"#jsExtensionBaseModalId > div.Container-sc-1tzcbkm-1.gNfIMq > div > div.Flex-sc-sqmtka-0.TableContainer-sc-ybu0mp-1.bXUgal.hhoMvF > div.Flex-sc-sqmtka-0.Container-sc-n6pzpt-0.eQnaRt.huoEMs > div:nth-child(2) > div.Flex-sc-sqmtka-0.ftsCjc > button > div > div")
                    print("->", updatedContent.text)
                    if updatedContent.text != "Charger plus de résultats" and updatedContent.text != "Loading...":
                        stillRecherche = False
                    elif updatedContent.text == "Charger plus de résultats" :
                        stillRecherche = True
                except Exception as ec:
                    stillRecherche = False
            jsBtn = self.find_element(By.CSS_SELECTOR,"#jsExtensionBaseModalId > div.Container-sc-1tzcbkm-1.gNfIMq > div > div.Flex-sc-sqmtka-0.TableContainer-sc-ybu0mp-1.bXUgal.hhoMvF > div.Flex-sc-sqmtka-0.Container-sc-n6pzpt-0.eQnaRt.huoEMs > div:nth-child(1) > div.Flex-sc-sqmtka-0.kGVKPL > div > div > div")
            print("we'll start downloading")
            jsBtn.click()
            time.sleep(5)
            # jsBtn = self.find_element(By.CSS_SELECTOR,"#radix-\:r22e\: > div > div:nth-child(1)")
            # jsBtn = self.find_element(By.CSS_SELECTOR,"#radix-\:rsq\: > div > div:nth-child(1)")
            jsBtn = self.find_elements(By.CSS_SELECTOR, ".Flex-sc-sqmtka-0.Container-sc-6f3o0q-0.ftsCjc.Aroud")[0]
            print("download")
            jsBtn.click()
        except ZeroDivisionError:
            print("Jungle Scout Exception please contact your administrator!")
