from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def get_product_list():
    url = "https://www.amazon.com.mx/s?k=funko+pop&crid=MWVW5UNW0707&sprefix=%2Caps%2C393&ref=nb_sb_ss_recent_1_0_recent"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "lxml") 
    a_class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
    a_tags = soup.find_all("a", class_=a_class)

    for a in a_tags:
        title = a.text.replace("\n", "")
        link = a.get("href") 
        print("título: ", title)
        print("link: ", link)
        print("\n")

        detail_link = "https://www.amazon.com.mx" + link if "https" not in link else link 
        get_details(detail_link)

def get_details(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")

    price_class = "a-section a-spacing-none aok-align-center aok-relative"
    price = float(soup.find("span", class_=price_class).text.replace("$", "").replace(",", ""))
    print("price: ", price)

    description_id = "a-section a-spacing-small"
    description = soup.find("div", id=description_id).text
    print("description: ", description)

get_product_list()
driver.close()

