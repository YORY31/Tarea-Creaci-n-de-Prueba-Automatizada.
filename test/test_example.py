import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_try_it_yourself():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20) 
    

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    try:
        driver.get("https://www.w3schools.com/html/")
        assert "HTML" in driver.title  

       
        try_it_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='w3-btn w3-margin-bottom' and @target='_blank']"))
        )
        try_it_link.click() 

        
        driver.switch_to.window(driver.window_handles[1])
        assert "Tryit" in driver.title  

        
        driver.save_screenshot("screenshots_video/try_it_yourself.png")
        
    finally:
        driver.quit()  


test_try_it_yourself()
