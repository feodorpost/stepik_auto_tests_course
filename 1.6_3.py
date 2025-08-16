from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

link= "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Ответик")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    keyboard.wait("esc")
    browser.quit()


