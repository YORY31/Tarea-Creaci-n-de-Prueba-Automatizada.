from selenium import webdriver
from selenium.webdriver.common.by import By

def test_forms():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.w3schools.com/html/html_forms.asp")
        assert "HTML Forms" in driver.title

      
        driver.find_element(By.ID, "fname").send_keys("John")
        driver.find_element(By.ID, "lname").send_keys("Doe")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        driver.save_screenshot("screenshots_video/form_submission.png")
    finally:
        driver.quit()
