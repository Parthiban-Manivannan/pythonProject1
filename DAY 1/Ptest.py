# test_login.py
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    """Test successful login on the website."""
    driver.get("https://www.linkedin.com/home")

    # Find elements
    username_field = driver.find_element(By.XPATH, "//input[@id='session_key']")
    password_field = driver.find_element(By.XPATH, "//input[@id='session_password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")

    # Enter credentials
    username_field.send_keys("parthi14199@gmail.com")
    password_field.send_keys("@MGRMouth007")

    # Click login button
    login_button.click()

    # Wait for successful login message
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@title='Home']"))
    )

    assert success_message.text == "Home"

def test_login_failure(driver):
    """Test failed login attempt with invalid credentials."""
    driver.get("https://www.linkedin.com/home")

    # Find elements
    username_field = driver.find_element(By.XPATH, "//input[@id='session_key']")
    password_field = driver.find_element(By.XPATH, "//input[@id='session_password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")

    # Enter invalid credentials
    username_field.send_keys("parthi14199@gmail.com")
    password_field.send_keys("@MGRMouth00")

    # Click login button
    login_button.click()

    # Wait for error message
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='error-for-password']"))
    )

    assert error_message.text == "Wrong email or password. Try again or create an accoun ."

# Fixtures to setup and teardown webdriver instance
@pytest.fixture
def driver():
    """Provides a Chrome webdriver instance for each test."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

