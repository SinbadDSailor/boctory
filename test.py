#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time



options = Options()
options.add_experimental_option('detach', True)
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
driver.get("https://www.9gag.com")
print(driver.title)

time.sleep(3)

for i in range(1,5):

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('article')

    for post in posts:
        a = post.find('h2')
        print(a)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    

driver.quit()

