#!/usr/bin/env python3
import os.path, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_html_win_selen(url):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
# #---------------------------------------------Screenshot----------------------------------------------|
#     time.sleep(3)
#     driver.set_window_size(1200, 14000)
#     if not os.path.exists("img/"):
#        os.makedirs("img/")
#     driver.save_screenshot(f'img/screen.png')
# #---------------------------------------------Screenshot----------------------------------------------|
    response = driver.page_source
    driver.close()
    driver.quit()

    return response
