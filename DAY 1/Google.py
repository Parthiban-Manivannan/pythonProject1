from selenium import webdriver
from selenium.webdriver import Keys
def google_search(query):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    return driver.title

if __name__ == "__main__":
    print(google_search("How to automate Google search with Python"))