from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from auth_data import username,password
import time
import random


def hashtag_search(username, password, hashtag):
    browser = webdriver.Chrome('instagram\chromedriver.exe')
    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(5,7))

        username_input = browser.find_element(By.NAME,'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(random.randrange(4,6))

        password_input = browser.find_element(By.NAME,'password')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(random.randrange(4,6))

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(4,6))

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}')
            time.sleep(random.randrange(4,7))
            
            hrefs = browser.find_elements(By.TAG_NAME,'a')

            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
                                    
            
            for url in posts_urls[0:5]:
                browser.get(url)
                time.sleep(random.randrange(5,9))
                like_button = browser.find_element(By.CSS_SELECTOR,'section:first-child span button').click()
                time.sleep(random.randrange(5,8))
                            
        except Exception as ex:
            print (ex)
            browser.close()
            browser.quit()
        
        browser.close()
        browser.quit()

    except Exception as ex:
        print (ex)
        browser.close()
        browser.quit()

hashtag_search(username, password,'belarustravel')