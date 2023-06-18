import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image

class Searching(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Searching, self).__init__()
        # self.implicitly_wait(100)
        self.maximize_window()
        self.collection = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        else:
            input('Press Any key to close the program and press enter')

    def land_first_page(self, query=""):
        if (query == ""):
            self.get(const.BASE_URL)
        else:
            self.get(const.BASE_URL + f"/s?k={query.replace(' ', '+')}")

    def getPage(self, query=''):
        if (query == ""):
            self.get(const.BASE_URL)
        else:
            self.get(const.BASE_URL + query)

    def close_PoP_Up(self):
        try:
            closebtn = self.find_element(
                By.ID,
                'sp-cc-rejectall-link'
            )
            closebtn.click()
        except:
            pass

    def AmNotARobot(self):
        try:
            # self.implicitly_wait(100)
            time.sleep(10)
            input = self.find_element(
                By.ID,"captchacharacters"
            )
            image_link = self.find_element(
                By.CLASS_NAME,"a-row a-text-center"
            ).find_element(By.TAG_NAME,"img").text.strip()
            print("The image url is ",image_link)
            # self.find_element(By.CLASS_NAME,"a-button-text").click()
        except:
            pass

    def search(self, query):
        searchBar = self.find_element(
            By.ID,
            "twotabsearchtextbox"
        )
        searchBar.send_keys(query)
        searchBtn = self.find_element(
            By.ID,
            "nav-search-submit-button"
        )
        searchBtn.click()

    def getHtmlSource(self):
        return self.page_source

    def getFirstDataFrame(self):
        # WebDriverWait(self, 120).until(
        #     EC.presence_of_element_located(
        #         (By.CLASS_NAME, 'a-size-medium-plus')
        #     )
        # )
        time.sleep(10)
        # self.implicitly_wait(100)
        htmlcontent = self.getHtmlSource()
        # with open("test.html", "w") as file:
        #     file.write(htmlcontent)
        # self.implicitly_wait(100)
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        articles = soup.find_all('div', class_=['s-card-container', 's-overflow-hidden'])
        for article in articles:
            try:
                product_name = article.find('span',
                                            class_='a-size-base-plus').text.strip()
                link = article.find('a',
                                    class_='a-link-normal')
                # Append the extracted data to the collection
                self.collection.append({
                    'product_name': product_name,
                    'Product_link': link['href']
                })
            except:
                pass
        # self.implicitly_wait(100)
        try:
            suivantBtn = self.find_element(
                By.CSS_SELECTOR,
                "a.s-pagination-next"
            )
            suivantBtn.click()
            # self.implicitly_wait(100)
            return self.getFirstDataFrame()
        except:
            return self.collection

    def getSecondDataFrame(self, df):
        for i in df.itertuples():
            link = i.Product_link
            with Searching() as bot:
                bot.getPage(link)
                bot.AmNotARobot()
                bot.close_PoP_Up()
                # time.sleep(10)
                # htmlcontent = self.getHtmlSource()
                # with open("test.html", "w") as file:
                #     file.write(htmlcontent)
                # soup = BeautifulSoup(htmlcontent, 'html.parser')
                try:
                    btn = bot.find_element(
                        By.CLASS_NAME, "a-expander-prompt"
                    )
                    btn.click()
                except:
                    pass
                # Get the price
                try:
                    price = bot.find_element(
                        By.CLASS_NAME, "a-price-whole"
                    ).text.strip()
                    try:
                        pricess = bot.find_element(
                            By.CLASS_NAME, "a-price-fraction"
                        ).text.strip()
                    except:
                        pricess = 0
                    print(price + "." + pricess)
                    price += "." + pricess
                except:
                    price = None
                    print("Can't Find the price")
                # Get the ranking
                try:
                    ranks = bot.find_element(
                        By.ID, "averageCustomerReviews"
                    ).find_element(By.CSS_SELECTOR, "span.a-size-base.a-color-base").text.strip()
                    print(ranks)
                except:
                    ranks = None
                    print("Can't find the ranks")
                # Get the Bullet Points
                try:
                    bloc = bot.find_element(
                        By.ID, "feature-bullets"
                    )
                    bullets = bloc.find_elements(
                        By.CSS_SELECTOR, "span.a-list-item"
                    )
                    bullet_points = [bullet.text for bullet in bullets]
                    print(bullet_points)
                except:
                    bullet_points = None
                    print("Can't find the bullet points")
                # Get the comments

                # Get all type of messages
                try:
                    bot.find_element(
                        By.ID, "cm-cr-dp-review-sort-type"
                    ).find_element(
                        By.CSS_SELECTOR,
                        'option[value="recent"]'
                    ).click()
                except:
                    pass

                try:
                    time.sleep(10)
                    CommentBody = bot.find_elements(
                        By.CSS_SELECTOR,
                        'div[data-hook="review"]'
                    )
                    comments = {}

                    for i in CommentBody:
                        try :
                            title = i.find_element(
                                By.CSS_SELECTOR,
                                'a[data-hook="review-title"]'
                            ).find_element(By.TAG_NAME,"span").text.strip()
                            content = i.find_element(
                                By.CSS_SELECTOR,
                                'span[data-hook="review-body"]'
                            ).find_element(By.TAG_NAME,"span").text.strip()
                            print(title,content)
                        except:
                            title = i.find_element(
                                By.CSS_SELECTOR,
                                'span[data-hook="review-title"]'
                            ).find_element(By.TAG_NAME, "span").text.strip()
                            content = i.find_element(
                                By.CSS_SELECTOR,
                                'span[data-hook="review-body"]'
                            ).find_element(By.CSS_SELECTOR, 'span[class="cr-original-review-content"]').text.strip()
                            print(title, content)


                    # bot.implicitly_wait(100)
                    # titles = bot.find_elements(
                    #     By.CSS_SELECTOR,
                    #     'a[data-hook="review-title"]'
                    # )
                    # bot.implicitly_wait(100)
                    # # titless = bot.find_elements(
                    # #     By.CSS_SELECTOR,
                    # #     'span[data-hook="review-title"]'
                    # # )
                    # # contents = bot.find_elements(
                    # #     By.CSS_SELECTOR,
                    # #     'div[class="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"]'
                    # # )
                    # comments = {}
                    # # for i, j in enumerate(titles):
                    # #     # comments[j.find_element(By.TAG_NAME,"span").text.strip()] = contents[i].find_element(By.TAG_NAME,"span").text.strip()
                    # #     comments[j.find_element(by=By.TAG_NAME,value='span')] = ""
                    # for i in titles:
                    #     try:
                    #         print(i.find_element(by=By.TAG_NAME, value='span').text.strip())
                    #     except:
                    #         print(i)
                    # # for i in titless:
                    # #     try :
                    # #         print(i.find_element(by=By.TAG_NAME,value='span').text.strip())
                    # #     except:
                    # #         print(i)
                    # # print(contents)
                    # # print(comments)
                    # # for i in contents:
                    # #     # print(i.find_element(By.TAG_NAME,'span').text.strip())
                    # #     try:
                    # #         print(i.find_element(By.CSS_SELECTOR,'span[class="cr-original-review-content"]'))
                    # #     except:
                    # #         try:
                    # #             print(i.find_element(By.TAG_NAME,"span"))
                    # #         except:
                    # #             pass
                except ZeroDivisionError:
                    comments = None
                    print("Can't find the comments")
            break
