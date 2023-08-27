from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

def google_search(query):
    driver = selenium.webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    return driver.title

if __name__ == "__main__":
    print(google_search("How to automate Google search with Python"))