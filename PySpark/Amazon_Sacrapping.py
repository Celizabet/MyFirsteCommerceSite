from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
all_products_list = []
i = 0

def getAllProducts():
    url = "https://www.amazon.com.mx/s?k=bailando+juntos+yuya&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1AHJFFIJ7NPMI&sprefix=bailando+juntos+yuya%2Caps%2C328&ref=nb_sb_noss_1"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "lxml")
    a_class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
    a_tags = soup.find_all("a", class_=a_class)
    
    for a in a_tags:
        product = {}
          
        product["Product Name "] = a.text.replace("\n", " ").replace(",", "+")
        product["Link "] = a.get("href") 
        
        link = a.get("href")
        detail_link = "https://www.amazon.com.mx/" + link if "https" not in link else link
        
        product["Price "] = getProductPrice(detail_link)
        product["Description "] = getProductDescription(detail_link)
            
        all_products_list.append(product)
    
    print(all_products_list)


def getProductPrice(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")

    price_class = "a-price-whole"
    if soup.find("span", class_=price_class):
        price = float(soup.find("span", class_=price_class).text.replace("$", "").replace(",", ""))
    else:
        price = 0
    
    return price 
    
    
def getProductDescription(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    
    description_class = "a-spacing-mini"
    desc_tags = soup.find_all("li", class_=description_class)
    
    description = []
    for a in desc_tags:
        description.append(a.text.replace("\n", "").replace(",", "+"))
    
    return description


df = pd.DataFrame(all_products_list)
df.to_csv("AmazonProductsFile.csv")