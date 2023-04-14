
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a Service instance with the path to chromedriver.exe
s = Service("C:\\Selenium\\chromedriver.exe")

# Create a webdriver instance with the Service
driver = webdriver.Chrome(service=s)

# Create a WebDriverWait instance with the driver and a timeout of 10 seconds


# Navigate to Google homepage
driver.get("https://www.google.com")
driver.maximize_window()

# Find the search box element and enter "Selenium" as search query
sbox = driver.find_element(By.NAME, 'q')
sbox.send_keys("Selenium")
sbox.submit()

# Wait for the search results page to load and find the first search result link
mywait = WebDriverWait(driver, 50)
s = mywait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Selenium' and @class='LC20lb MBeuO DKV0Md']")))
s.click()

# Close the webdriver instance
driver.close()

