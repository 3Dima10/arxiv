from selenium import webdriver
import time

url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="C:\\личные\\програма\\pythonProject\\Firefoxs\\chromedriver.exe")
try:
    driver.get(url="https://www.whati")
    time.sleep(5)
except Exception as ex :
    print(ex)
finally:
    driver.close()
    driver.quit()