from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

sbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("kl")
time.sleep(5)
try:
    print("Display status:",sbox.is_displayed())
    print("Enabled status:",sbox.is_enabled())
except:
    print("Exception")
time.sleep(5)
# driver.close()




