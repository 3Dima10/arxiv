from selenium import webdriver
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
browes = webdriver.Chrome(
    executable_path="C:\\личные\\програма\\pythonProject\\Firefoxs\\chromedriver.exe",
    options=options)
browes.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
