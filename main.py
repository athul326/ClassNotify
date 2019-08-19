from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import os
import time
import classList
import apikeys

# sends message to appropriate user's phone number informing them of class opening, uses Twilio API
def message(text):
    from twilio.rest import Client
    account_sid = apikeys.accountID  # requires Twilio account and authorized number to send messages from
    auth_token = apikeys.authKey
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=text,
            from_=apikeys.fromNumber,
            to=apikeys.toNumber
    )

# uses Selenium to navigate to appropriate page and scrape through given classes and check availability
def search(driver):
    driver.get("https://compassxe-ssb.tamu.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")
    # selects the appropriate semester in the combobox element
    combobox = driver.find_element_by_id("s2id_txt_term")
    combobox.click()
    term_input = driver.find_element_by_id("s2id_autogen1_search")
    term_input.send_keys("Fall 2019 - College Station")
    term_input.click()
    time.sleep(0.5)
    term_input.send_keys(Keys.RETURN)
    time.sleep(0.5)
    term_next = driver.find_element_by_id("term-go")
    term_next.click()
    time.sleep(0.5)
    # for loop that goes through and checks availability for every class in the userClasses dictionary
    for x in classList.userClasses:
        # selects course text box and inputs course
        subject_box = driver.find_element_by_id("s2id_txt_subject")
        subject_box.click()
        subject_input = driver.find_element_by_id("s2id_autogen1")
        # first four characters of the dictionary key correspond to the course department
        subject_input.send_keys(x[0:4])
        time.sleep(0.75)
        subject_input.send_keys(Keys.RETURN)
        course_input = driver.find_element_by_id("txt_courseNumber")
        # last three characters of the dictionary key correspond to course number
        course_input.send_keys(x[5:10])
        class_next = driver.find_element_by_id("search-go")
        class_next.click()
        time.sleep(0.5)
        # makes the page display the max number of courses
        size_list = Select(driver.find_element_by_class_name("page-size-select"))
        size_list.select_by_value("50")
        time.sleep(0.5)
        # BeautifulSoup used to search through table of courses
        page_source = BeautifulSoup(driver.page_source,'lxml')
        # for loop goes through every row in table of courses
        for tr in page_source.find_all('tr')[1:]:
            tds = tr.find_all('td')
            # for loop goes through given course sections and checks if there is availability
            for sections in classList.userClasses[x]:
                if tds[1].text == sections:
                    if "FULL" not in tds[10].text:
                        text_send = x + ' - ' + classList.userClasses[x] + ' has open seats'
                        message(text_send)  # sends message if there is availability in given section
        # goes through and resets page to get ready for the next course search
        search_again = driver.find_element_by_id("search-again-button")
        search_again.click()
        time.sleep(0.5)
        reset_button = driver.find_element_by_class_name("select2-search-choice-close")
        reset_button.click()
        course_input.clear()


def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver = os.getcwd() + "\\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    # endless loop to keep program running and search for classes every 5 minutes to not overload the server
    while True:
        search(driver)
        time.sleep(300)
