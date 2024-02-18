from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

sbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
a=sbox.is_displayed()
b=sbox.is_enabled()

if a==True:
    print('Sbox is Test Passed')

driver.close()




