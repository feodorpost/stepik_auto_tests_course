from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fname_input = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
    fname_input.send_keys("Feodor")
    time.sleep(1)
    lname_input = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    lname_input.send_keys("Shel")
    time.sleep(1)
    email_input = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
    email_input.send_keys("usualemail@mail.com")
    time.sleep(1)
    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    keyboard.wait("esc")
    browser.quit()
