from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

# Ссылка на целевую страницу
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    # Имя
    fname_input = browser.find_element(By.XPATH, "//input[@class='form -control first' and @required]")
    fname_input.send_keys("Feodor")
    time.sleep(1)
    # Фамилия
    lname_input = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    lname_input.send_keys("Post")
    time.sleep(1)
    # Электронная почта
    email_input = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required]")
    email_input.send_keys("usualemail@mail.com")
    time.sleep(1)
    # Кнопка "Submit"
    button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()

    time.sleep(1)

    # Проверка, сходится ли конечный текст с искомым
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Закрытие окна браузера не по таймеру как в курсе, а по нажатию кнопки "Esc" на клавиатуре
    keyboard.wait("esc")
    browser.quit()
