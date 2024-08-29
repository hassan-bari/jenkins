from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

try:
    # Step 1: Open Google.com
    driver.get("https://www.google.com")

    # Assert that Google.com is opened
    assert "Google" in driver.title, "Google.com did not open successfully."

    # Step 2: Search for "cars"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("cars")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(2)

    # Assert that the search was performed
    assert "cars" in driver.title, "Search for 'cars' was not successful."

finally:
    # Close the browser
    driver.quit()
