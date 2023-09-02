

from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# caro=driver.find_elements(By.CLASS_NAME,'a-carousel-card')
# print(len(caro))
# links=driver.find_elements(By.TAG_NAME,'a')
# print(len(links))
# print(driver.title)
# print(driver.current_url)
# search_box=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
# print(search_box.is_enabled())
# print(search_box.is_displayed())
# driver.get("https://www.google.com")
# driver.back()
# time.sleep(10)
# driver.refresh()
# driver.forward()
# driver.get("https://demo.nopcommerce.com/")
# sbox = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(sbox))
# link1=driver.find_elements(By.XPATH,"//div[@class='footer-block information']//ul//a")
# print(len(link1))
# for x in link1:
#     print(x.text)
# a=driver.find_elements(By.PARTIAL_LINK_TEXT,"Log")
# print(len(a))
wait=WebDriverWait(driver,10)
driver.get("https://demo.nopcommerce.com/login")
# element=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='Email']")))
# element.click()
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()

emailbox.send_keys("parthi14199@gmail.com")
print(emailbox.get_attribute('value'))
driver.close()








