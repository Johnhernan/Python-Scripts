from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == "__main__":
    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    # ----------- Cheat Sheet --------------
    # Find by name attribute
    # search_bar = driver.find_elements_by_name("q")

    # Get an atribute
    # print(search_bar.get_attribute("placeholder"))
    # print(search_bar.tag_name)

    # Find by Class
    # logo = driver.find_element_by_class_name("python-logo")
    # print(logo.size)

    # Find by css selector
    # doc_link = driver.find_element_by_css_selector(".documentation-widget a")
    # print(doc_link.text)

    # Find by xpath
    # driver.find_element_by_xpath('//*[@id="tabs--1-tab-5"]/span')

    # Find by link text
    # all_portals = driver.find_element_by_link_text("All portals")
    # all_portals.click()

    # Type in the browser
    # search = driver.find_element_by_name("search")
    # search.send_keys("Python")
    # search.send_keys(Keys.ENTER)

    # ----------- Python main page event list  --------------
    # events = driver.find_elements_by_css_selector(".event-widget  li a")
    # days_data = driver.find_elements_by_css_selector(".event-widget  li time")
    # days = [day.get_attribute("datetime").split(":")[0].split("T")[0] for day in days_data]
    #
    # upcoming_events = {}
    # for n in range(len(days)):
    #     upcoming_events[n] = {
    #         "time": days[n],
    #         "event": events[n].text
    #     }
    #
    # print(upcoming_events)
    # article_count = driver.find_element_by_css_selector("#articlecount a")
    # print(article_count.text)

    # ----------- Cookie clicker cheat Script  --------------
    cookie = driver.find_element_by_id("cookie")
    click_counter = 0
    while click_counter <= 2005:
        upgrades = [upgrade for upgrade in driver.find_elements_by_css_selector("#store div")[:-1]
                    if upgrade.get_attribute("class") != "amount"]

        for upgrade in upgrades[::-1]:
            is_buyable = upgrade.get_attribute("class")
            if is_buyable != "grayed":
                upgrade.click()
                break
            else:
                cookie.click()
                click_counter += 1

    wallet = driver.find_element_by_id("money")
    print(wallet.text)

    driver.quit()
