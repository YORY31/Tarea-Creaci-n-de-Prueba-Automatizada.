from selenium import webdriver
from selenium.webdriver.common.by import By
def test_navigation():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.w3schools.com/html/")
        assert "HTML" in driver.title

        
        driver.find_element(By.LINK_TEXT, "HTML Tables").click()
        assert "HTML Tables" in driver.title
        driver.save_screenshot("screenshots/navigation_to_tables.png")

       
        driver.find_element(By.LINK_TEXT, "HTML HOME").click()
        assert "HTML" in driver.title
        driver.save_screenshot("screenshots_video/back_to_home.png")
    finally:
        driver.quit()