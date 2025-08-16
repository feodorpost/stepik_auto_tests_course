from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Feodor")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Shel")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Prm")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Rus")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    keyboard.wait("esc")
    browser.quit()