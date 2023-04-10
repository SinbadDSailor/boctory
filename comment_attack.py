from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.file_detector import UselessFileDetector
import time
import random
import json
import os
import sqlite3
from sqlite3 import Error
from ngbot import NgPropagator


class Commenter(NgPropagator):

    def post_finder(self, tag):
        driver = self.get_driver()
        json_file = "storage/temp_com.json"
        my_dict = {}
        driver.get(f"https://9gag.com/tag/{tag}?ref=search")
        time.sleep(3)

        for i in range(5):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

            html = driver.page_source

            soup = BeautifulSoup(html, 'html.parser')
            posts = soup.find_all('article')

            for post in posts:
                post_box = post.find('h2')
                try:
                    pb_string = str(post_box.contents)
                    name_key = pb_string[2:-2]
                    get_parent = post_box.parent
                    get_url = get_parent.attrs.get('href')
                    full_link = 'https://9gag.com' + get_url
                    #print('Title: ' + name_key + '\nLink: ' + full_link)
                    # print('--------------------------------------')
                    my_dict[str(name_key)] = str(full_link)
                except AttributeError:
                    pass

            time.sleep(1)

        # for item in my_dict:
        #    print(item + ' -> ' + my_dict[item])
        # print(my_dict)
        driver.quit()
        js = json.dumps(my_dict, indent=4)
        fp = open(json_file, "w+")
        fp.write(js)
        fp.close()
        # return my_dict

    def post_random(self, tag):
        file_location = "storage/temp_com.json"
        if os.path.exists(file_location) == False:
            open(file_location, "w+")

        if os.stat(file_location).st_size == 0:
            self.post_finder(tag)

        with open(file_location, 'r') as myfile:
            json_data = myfile.read()
        obj = json.loads(json_data)
        key, value = random.choice(list(obj.items()))
        return key, value

    def comment_random(self, file_location):
        comments_txt_file = open(file_location, 'r')

        file_lines = comments_txt_file.read()
        cut_file_lines = file_lines.replace("\n", "")

        separated_lines = cut_file_lines.split(",")

        random_comment = random.choice(separated_lines)

        comments_txt_file.close()
        return random_comment[1:-1]

    def post_comment(self, number_of_posts, file_location, tag, email, password):

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

        # POST COMMENT BLOCK ------------------>
        for num in range(number_of_posts):
            comment = self.comment_random(file_location)
            key, value = self.post_random(tag)
            url = value + '#comment'
            print(f'Current post is ---> {key}')
            print(f'Current comment is ---> {comment}')
            print("---------------------------------------------------")

            # Open a new window
            driver.execute_script("window.open('');")

            # Switch to the new window and open new URL
            driver.switch_to.window(driver.window_handles[1])
            driver.get(url)
            time.sleep(5)

            # Leave a comment in post
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[class='comment-input-area-content__input-area_textarea']"))).send_keys(comment)
            time.sleep(5)
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//button[@class='ui-btn btn-color-primary btn-round-light']"))).click()

            # Closing new_url tab
            driver.close()

            # Switching to old tab
            driver.switch_to.window(driver.window_handles[0])


        # POST COMMENT BLOCK -----------------/>


        # LOGOUT BLOCK ------------------->
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='avatar-container']"))).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log Out']"))).click()
        time.sleep(2)
        # LOGOUT BLOCK ------------------/>


        driver.quit()



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
    id_grabber = int(input('Enter id of a bot you want to use: '))
    number_of_posts = int(input('Enter number of posts you want to leave a comment in: '))
    tag = 'ukraine'
    bot_num = Utility()
    email, password = bot_num.credentials_grabber(id_grabber)
    bot = Commenter()
    bot.post_comment(number_of_posts, 'test.txt', tag, email, password)

    # bot.post_finder('ukraine')


if __name__ == '__main__':
    main()
