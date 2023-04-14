from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

sbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",sbox.is_displayed())
print("Enabled status:",sbox.is_enabled())

driver.close()