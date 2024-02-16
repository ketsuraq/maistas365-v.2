from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def scrape_data():
    url = 'https://eparduotuve.iki.lt/product/IKI/Arbatinukas-11l'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    title = soup.title.string.strip().split('|')[0].strip()

    driver = webdriver.Chrome()
    driver.get(url)

    def get_element_text(driver, xpath):
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element.text
        except (TimeoutException, NoSuchElementException):
            return "Not found"

    about = get_element_text(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div[1]/div[2]/div[4]/span[1]')
    euros = get_element_text(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div/h1')
    cents = get_element_text(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div/span[2]')
    price = "€ " + euros + "." + cents
    discount = get_element_text(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/span/span/div/span')

    driver.quit()

    return title, about, price, discount

if __name__ == "__main__":
    title, about, price, discount = scrape_data()
    print(f"Title: {title}")
    print(f"About: {about}")
    print(f"Price: {price}")
    print(f"Discount: {discount}")