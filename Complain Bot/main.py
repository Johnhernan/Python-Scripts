from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"C:\Development\chromedriver.exe"
TWITTER_EMAIL = "foo"
TWITTER_PASSWORD = "foo"

if __name__ == '__main__':
    internet_speed_twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
    download_speed = internet_speed_twitter_bot.get_internet_speed()

    if download_speed < PROMISED_DOWN:
        download_speed = 30
        internet_speed_twitter_bot.tweet_at_provider(username=TWITTER_EMAIL,
                                                     password=TWITTER_PASSWORD,
                                                     current_speed=download_speed,
                                                     promised_speed=PROMISED_DOWN)
