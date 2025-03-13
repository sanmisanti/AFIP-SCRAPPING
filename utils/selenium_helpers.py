"""Helper functions for Selenium operations."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def initialize_driver(headless=True):
    """Initialize and return a Chrome WebDriver instance."""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    return webdriver.Chrome(options=chrome_options)

def wait_for_element(driver, locator_type, locator_value, timeout=10, clickable=False):
    """Wait for an element to be present or clickable."""
    wait = WebDriverWait(driver, timeout)
    if clickable:
        return wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
    else:
        return wait.until(EC.presence_of_element_located((locator_type, locator_value)))

def set_input_value_js(driver, element, value):
    """Set an input value using JavaScript."""
    driver.execute_script(f"arguments[0].value = '{value}';", element)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", element)
    driver.execute_script("arguments[0].dispatchEvent(new Event('blur'));", element)