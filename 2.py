# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import sys
# import time
#
# try:
#     link = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- функция для вычисления ---
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     # --- находим x и считаем y ---
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     # --- вводим ответ ---
#     answer_input = browser.find_element(By.ID, "answer")
#     answer_input.send_keys(y)
#
#     # --- отмечаем чекбокс и радиокнопку ---
#     robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
#     robot_checkbox.click()
#     robots_rule_radio = browser.find_element(By.ID, "robotsRule")
#     robots_rule_radio.click()
#
#     # --- нажимаем Submit ---
#     submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     submit_button.click()
#
#     # --- выводим число в консоль без лишних символов ---
#     sys.stdout.write(y)
#     sys.stdout.flush()
#
#     time.sleep(10)  # чтобы успеть увидеть результат на странице
#
# finally:
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import sys
# import time
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- функция для вычисления ---
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     # --- находим сундук и получаем x из атрибута valuex ---
#     chest_img = browser.find_element(By.ID, "treasure")
#     x = chest_img.get_attribute("valuex")
#     y = calc(x)
#
#     # --- вводим ответ ---
#     answer_input = browser.find_element(By.ID, "answer")
#     answer_input.send_keys(y)
#
#     # --- отмечаем чекбокс и радиокнопку ---
#     robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
#     robot_checkbox.click()
#     robots_rule_radio = browser.find_element(By.ID, "robotsRule")
#     robots_rule_radio.click()
#
#     # --- нажимаем Submit ---
#     submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     submit_button.click()
#
#     # --- выводим число в консоль без лишних символов ---
#     sys.stdout.write(y)
#     sys.stdout.flush()
#
#     time.sleep(2)  # чтобы увидеть результат на странице
#
# finally:
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- находим числа и считаем сумму ---
#     num1 = browser.find_element(By.ID, "num1").text
#     num2 = browser.find_element(By.ID, "num2").text
#     total = str(int(num1) + int(num2))  # обязательно str для выбора в Select
#
#     # --- выбираем значение в выпадающем списке ---
#     select_element = browser.find_element(By.TAG_NAME, "select")
#     select = Select(select_element)
#     select.select_by_value(total)  # выбираем по значению
#
#     # --- нажимаем Submit ---
#     submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     submit_button.click()
#
#     time.sleep(5)  # чтобы увидеть результат на странице
#
# finally:
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import time
#
# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- функция для вычисления ---
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     # --- находим x ---
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     # --- прокручиваем страницу до поля ввода ---
#     answer_input = browser.find_element(By.ID, "answer")
#     browser.execute_script("arguments[0].scrollIntoView(true);", answer_input)
#     answer_input.send_keys(y)
#
#     # --- отмечаем чекбокс и радиокнопку ---
#     robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
#     browser.execute_script("arguments[0].scrollIntoView(true);", robot_checkbox)
#     robot_checkbox.click()
#
#     robots_rule_radio = browser.find_element(By.ID, "robotsRule")
#     browser.execute_script("arguments[0].scrollIntoView(true);", robots_rule_radio)
#     robots_rule_radio.click()
#
#     # --- нажимаем Submit ---
#     submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
#     submit_button.click()
#
#     time.sleep(5)  # чтобы увидеть результат на странице
#
# finally:
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# import time
#
# try:
#     # --- создаем файл автоматически ---
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, "file.txt")
#     with open(file_path, "w") as f:
#         f.write("Это тестовый файл")
#
#     # --- открываем страницу ---
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- заполняем поля ---
#     browser.find_element(By.NAME, "firstname").send_keys("Иван")
#     browser.find_element(By.NAME, "lastname").send_keys("Иванов")
#     browser.find_element(By.NAME, "email").send_keys("ivan@example.com")
#
#     # --- загружаем файл ---
#     browser.find_element(By.ID, "file").send_keys(file_path)
#
#     # --- отправляем форму ---
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
#     time.sleep(2)
#
# finally:
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import time
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- Нажимаем кнопку, чтобы появился confirm ---
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
#     # --- Принимаем alert ---
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     # --- Считываем x и считаем функцию ---
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     # --- Вводим ответ ---
#     browser.find_element(By.ID, "answer").send_keys(y)
#
#     # --- Отправляем форму ---
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
#     time.sleep(5)  # чтобы увидеть результат
#
# finally:
#     browser.quit()

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import time
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # --- Нажимаем кнопку, которая открывает новую вкладку ---
#     browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
#
#     # --- Переключаемся на новую вкладку ---
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     # --- Считываем x и считаем функцию ---
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#
#     # --- Вводим ответ ---
#     browser.find_element(By.ID, "answer").send_keys(y)
#
#     # --- Отправляем форму ---
#     browser.find_element(By.CSS_SELECTOR, "button.btn").click()
#
#     time.sleep(2)  # чтобы увидеть результат
#
# finally:
#     browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, когда цена уменьшится до $100
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Отправляем решение
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Ждем несколько секунд, чтобы увидеть результат, затем закрываем браузер
    import time
    time.sleep(5)
    browser.quit()