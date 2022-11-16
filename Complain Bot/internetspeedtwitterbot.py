from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def get_internet_speed(self):
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://www.speedtest.net/")

        start_button = driver.find_element_by_class_name("start-text")
        start_button.click()
        time.sleep(50.0)
        download_speed = driver.find_element_by_class_name("download-speed")

        return float(download_speed.text)

    def tweet_at_provider(self, username, password, current_speed, promised_speed):
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://twitter.com/?lang=en")
        time.sleep(3)

        sign_up_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div')
        sign_up_button.click()
        time.sleep(3)

        username_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        username_box.send_keys('foo')
        username_box.send_keys(Keys.ENTER)
        time.sleep(3)

        username_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_box.send_keys(username)
        username_box.send_keys(Keys.ENTER)
        time.sleep(3)

        password_box = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input')
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(3)

        text_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
        text_box.send_keys(f"Why is my internet only {current_speed} instead of {promised_speed}")

        # tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        # tweet_button.click()