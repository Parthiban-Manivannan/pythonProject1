from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

act_title = driver.title
exp_title = "Logged In Successfully"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


