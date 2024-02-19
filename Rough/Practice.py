import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.get("https://www.google.com")
driver.back()
time.sleep(10)
driver.refresh()
driver.forward()
driver.get("https://demo.nopcommerce.com/")
sbox = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(sbox))
link1=driver.find_elements(By.XPATH,"//div[@class='footer-block information']//ul//a")
print(len(link1))
for x in link1:
    print(x.get_attribute('innerText'))
a=driver.find_elements(By.PARTIAL_LINK_TEXT,"Log")
print(len(a))
wait=WebDriverWait(driver,10)
driver.get("https://demo.nopcommerce.com/login")
element=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='Email']")))
element.click()
emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()

emailbox.send_keys("parthi14199@gmail.com")
print(emailbox.get_attribute('id'))
driver.get("http://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

list1=driver.find_elements(By.XPATH,"//*[@id='checkboxes']/input")
for x in list1:
    if x.is_selected():
        pass
    else:
        x.click()
for x in list1:
    if x.is_selected():
        x.click()
    else:
        pass

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,'a')
count=0
count2=0
for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,' is broken link')
        count+=1
    else:
        print(url, ' is valid link')
        count2 += 1

print('Total number of broken links:',count)
print('Total number of valid links:',count2)
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='first']"))
dropdown.select_by_visible_text("Iphone")
dropdown.select_by_index(0)
lenoptions=dropdown.options
print(len(lenoptions))
for x in lenoptions:
    print(x.text)
    if x.text=="Yahoo":
        x.click()
        pass
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

alertwin=driver.switch_to.alert
print(alertwin.text)
alertwin.send_keys("Welcome")
alertwin.accept()
alertwin.dismiss()

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
outframe=driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(outframe)
inframe=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(inframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
winID=driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
winID=driver.window_handles
parentwindow=winID[0]
childwindow=winID[1]
driver.switch_to.window(childwindow)
print(driver.title)
driver.switch_to.window(parentwindow)
print(driver.title)
for win in winID:
    driver.switch_to.window(win)
    if driver.title=="Your Store":
        driver.close()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[3]/div/span").click()
driver.find_element(By.XPATH,"//img[@alt='Mobiles']").click()
time.sleep(5)
a=Select(driver.find_element(By.XPATH,"//div[@class='_3uDYxP']//select[@class='_2YxCDZ']"))
options = a.options
for i in range(0, len(options), 2):
    print(options[i].text)
driver.get('https://cosmocode.io/automation-practice-webtable/')
driver.maximize_window()
noofrows=len(driver.find_elements(By.XPATH,"//table[@id='countries']//tr"))
noofcolumns=len(driver.find_elements(By.XPATH,"//table[@id='countries']//tr[1]//td"))
print(noofrows)
print(noofcolumns)

print("printing all the rows and columns data..")


driver.close()

























