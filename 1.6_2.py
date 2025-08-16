import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    target_link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    target_link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Feodor")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Shel")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Prm")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Rus")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    keyboard.wait("esc")
    browser.quit()


