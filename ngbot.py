#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.file_detector import UselessFileDetector
import time
from colors import colors


class Boctory():

    def __init__(self):
        pass

    def get_driver(self):

        PROXY = "110.34.3.229:3128"

        # SELENIUM SETUP BLOCK ------------->
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_argument('--no-sandbox')
        # options.add_argument('--proxy-server=%s' % PROXY) #****************WORKING****************
        # options.headless = True #Izvrsava operacije u pozadini, bez otvaranja prozora
        driver = webdriver.Chrome(options=options)
        driver.file_detector = UselessFileDetector()
        # SELENIUM SETUP BLOCK ------------/>
        return driver


class NgPropagator(Boctory):

    def login(self, email, password):
        driver = self.get_driver()
        driver.get("https://www.9gag.com")
        print(driver.title)
        time.sleep(2)
        # LOGIN BLOCK ------------------->
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-mute"))).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ui-btn btn-color-inherit signup-view__login']"))).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=''][name='username'][type='text']"))).send_keys(email)
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class=''][name='password'][type='password']"))).send_keys(password)
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ui-btn btn-color-primary login-view__login']"))).click()
        time.sleep(2)
        # LOGIN BLOCK ------------------/>

    def logout(self):
        driver = self.get_driver()
        # LOGOUT BLOCK ------------------->
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='avatar-container']"))).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log Out']"))).click()
        time.sleep(2)
        # LOGOUT BLOCK ------------------/>

    def post(self, title, tags, img_path):
        # POST BLOCK ------------------->
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='ui-btn btn-color-primary']"))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class='textarea'][name='title'][id='textarea']"))).send_keys(title)
        time.sleep(2)
        for tag in tags:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='upload-tag-input']"))).send_keys(tag)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(img_path)
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='toggle-button']"))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='ui-checkbox__field']"))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ui-btn btn-color-primary']"))).click()
        time.sleep(10)
        # POST BLOCK ------------------/>

        self.driver.quit()



class Utility:

    file_path = "storage/bots.db"

    def __init__(self):
        pass

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def credentials_grabber(self, id):
        #id_grabber = int(input("Enter ID of the bot you want to use: "))
        grab_comm = f"SELECT * FROM bots WHERE id = {id};"
        cont = self.create_connection(self.file_path)
        cursor = cont.cursor()

        cursor.execute(grab_comm)
        get_col = cursor.fetchone()

        cont.close()

        return get_col[2], get_col[3]


def main():
    # id_grabber = int(input("Enter ID of the bot you want to use: "))
    # bot_numb = Utility()
    # email, password = bot_numb.credentials_grabber(id_grabber)

    # print(f"{colors.BRED}**IMPORTANT**{colors.END} YOU ARE USING BOT WITH ID -> {colors.BRED}{id_grabber}{colors.END}")
    # print(f"EMAIL: {email}\nPASSWORD: {password}")

    # ngbot = NgPropagator()

    # tags = ("cats,", "dogs,", "funny,")

    # ngbot.login(email, password)
    # ngbot.post("test", tags, "/home/stspc/mp-bot/media/meme.jpeg")
    # ngbot.logout()
    print("OK")



if __name__ == "__main__":
    main()
