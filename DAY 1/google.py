import selenium
from selenium.webdriver.common.keys import Keys

def youtube_search(query):
    driver = selenium.webdriver.Chrome()
    driver.get("https://www.youtube.com")
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    first_video = driver.find_element_by_id("video-title")
    return first_video.text

if __name__ == "__main__":
    print(youtube_search("How to automate YouTube with Python"))
