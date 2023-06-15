from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read the HTML content from the file
with open('test.html', 'r') as file:
    html_content = file.read()

# Create BeautifulSoup object and parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
collection = []
articles = soup.find_all('div',class_=['s-card-container','s-overflow-hidden'])
for article in articles:
    product_name = article.find('span',
                                class_='a-size-base-plus').text.strip()
    link = article.find('a',
                        class_='a-link-normal')
    # Append the extracted data to the collection
    collection.append({
        'product_name': product_name,
        'Product_link':link['href']
    })

if(len(collection) == 0):
    print(f"hmmm lazem tal9a le vrai recherche ama thama nombre d'article is = {len(articles)}")
else :
    for i in collection:
        print(i)

