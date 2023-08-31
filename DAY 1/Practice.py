from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
caro=driver.find_elements(By.CLASS_NAME,'a-carousel-card')
print(len(caro))
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
print(driver.title)
print(driver.current_url)
search_box=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
print(search_box.is_enabled())
print(search_box.is_displayed())



driver.close()
