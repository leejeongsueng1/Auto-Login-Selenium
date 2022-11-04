import time
import sys
import os
import json
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def main():
    ID = ""
    PW = ""
    with open("user.json",'r') as f:
        credentials = json.load(f)
        ID = credentials["ID"]
        PW = credentials["PASSWORD"]

    config = ConfigParser()
    config.read("example.ini")
    CHROME_DRIVER_PATH = "driver/chromedriver.exe"
    DURATION = config.getint("delay", "seconds")

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)

    browser = webdriver.Chrome(resource_path(CHROME_DRIVER_PATH), options=options)
    URL = config.get("website", "url")
    browser.get(URL)

    time.sleep(DURATION)
    actions = ActionChains(browser)
    id_box = browser.find_element(By.ID,"loginIdtemp")
    actions.click(id_box)
    actions.perform()
    time.sleep(DURATION)
    browser.find_element(By.ID,"loginId").send_keys(f'{ID}'.strip())
    browser.find_element(By.ID,"loginId").send_keys(Keys.TAB)
    time.sleep(DURATION)
    browser.find_element(By.ID,"loginPw").send_keys(f'{PW}'.strip())
    time.sleep(DURATION)
    browser.find_element(By.ID,"loginPw").send_keys(Keys.ENTER)
    time.sleep(DURATION)

if __name__ == "__main__":
    main()