
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.find_element(By.ID,"username").send_keys("parthi14199@gmail.com")
driver.find_element(By.ID,"password").send_keys("@Arcplay007")
driver.find_element(By.XPATH,"//*[@id='organic-div']/form/div[3]/button").click()
driver.find_element(By.XPATH,"//span[@title='Jobs']").click()
time.sleep(5)
a=driver.find_element(By.XPATH,"//input[@role='combobox']")
a.send_keys('qa automation tester')
a.send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//div[@class='mt5']//div//div//div//button//span[@class='artdeco-button__text' and (text()='Apply' )]")








