#!/usr/bin/env python3
import os.path, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_html_lin_selen(url):
    service = Service("/usr/bin/chromedriver")
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("–no-sandbox")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    # #---------------------------------------------Screenshot----------------------------------------------|
    # time.sleep(3)
    # driver.set_window_size(1200, 14000)
    # if not os.path.exists("img/"):
    #     os.makedirs("img/")
    # driver.save_screenshot(f'img/screen.png')
    # #---------------------------------------------Screenshot----------------------------------------------|
    response = driver.page_source
    driver.close()
    driver.quit()
    
    return response
