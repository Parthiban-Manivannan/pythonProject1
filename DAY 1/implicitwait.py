from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(20)
driver.get("https://www.google.com")
driver.maximize_window()
sbox=driver.find_element(By.NAME,'q')
sbox.send_keys("Selenium")
sbox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium' and @Class='LC20lb MBeuO DKV0Md']").click()
