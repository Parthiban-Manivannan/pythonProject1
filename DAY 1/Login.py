from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys("student")
driver.find_element(By.NAME, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

act_title = driver.title
exp_title = "Logged In Successfully | Practice Test"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


