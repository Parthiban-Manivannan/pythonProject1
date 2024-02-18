from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def youtube_search(query):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    search_box = driver.find_element(By.XPATH, "//input[@id='search']")
    try:
        search_box.send_keys("How to automate YouTube with Python")
    except:
        print('Failed')
    search_box.send_keys(Keys.ENTER)
    first_video = driver.find_element(By.ID,"video-title")
    first_video.click()
    return first_video.text

if __name__ == "__main__":
    print(youtube_search("How to automate YouTube with Python"))


