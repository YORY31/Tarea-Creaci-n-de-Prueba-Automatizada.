from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_insert_youtube_video():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.w3schools.com/html/")
        assert "HTML" in driver.title


        wait = WebDriverWait(driver, 20)
        try_it_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Try it Yourself")))
        try_it_link.click()

       
        wait.until(EC.number_of_windows_to_be(2))  
        driver.switch_to.window(driver.window_handles[1])

        
        code_editor = wait.until(EC.visibility_of_element_located((By.ID, "textareaCode")))
        code_editor.send_keys('<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

   
        driver.save_screenshot("screenshots_video/insert_youtube_video.png")

       
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        assert iframe is not None 

    finally:
        driver.quit()


test_insert_youtube_video()
