from selenium import webdriver
from selenium.webdriver.common.by import By

def test_elements_visible():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.w3schools.com/html/")
        assert "HTML" in driver.title

 
        button = driver.find_element(By.LINK_TEXT, "HTML HOME")
        assert button.is_displayed()
        driver.save_screenshot("screenshots_video/button_visible.png")
    finally:
        driver.quit()
