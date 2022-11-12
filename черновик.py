from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def seleniumrt (a,pop ):
    driver = webdriver.Chrome(
        executable_path="C:\\личные\\програма\\pythonProject\\Firefoxs\\chromedriver.exe"
    )
    # открытее браузера

    try:
        driver.get(url="https://pomahach.com/search/")
        # открытия сайта " вси видповиди "

        v_input = driver.find_element(By.ID, "documentsearch-query")
        v_input.send_keys(a)  # слова пойска
        time.sleep(1)
        # поиск в поискавике сайта

        v_input.send_keys(Keys.ENTER)
        time.sleep(1)
        # ентер в поискавике

        lop = driver.find_element(By.CLASS_NAME, "gs-title").click()
        # открытие первой сылки
        pop = lop

        plus = driver.find_element(By.CLASS_NAME, "btn btn-success spoiler collapsed").click()
        # зеленая кнопка
        time.sleep(10)

    except Exception as ex:
        print(ex)
        # вывод ошыбки
    return a , pop


