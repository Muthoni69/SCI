from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Important for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, value="username").send_keys("student")
    driver.find_element(By.ID, value="password").send_keys("Password123")
    driver.find_element(By.ID, value="submit").click()

    assert driver.find_element(By.XPATH, value="//h1[contains(.,'Logged In Successfully')]").is_displayed()

def test_login_failure(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()

    error_msg = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error_msg


