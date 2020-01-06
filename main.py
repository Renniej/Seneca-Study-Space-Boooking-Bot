# Sources/Links of interest:
# Login Python Tutorial : https://www.hongkiat.com/blog/automate-create-login-bot-python-selenium/
# Seneca Room Booking : https://seneca.libguides.com/studyroom

# import libraries for web automation :)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Booking Link

Book_A_Study_Room_Link = 'https://seneca.libguides.com/studyroom'

# HTML IDs for campuses
King_Campus = 'kgLink'
Markham_Campus = 'mkLink'
York_Campus = 'syLink'
Newnham_Campus = 'nhLink'


# Booking Slots ID
Time_Grid = 's-lc-rm-time-grid'
Time_Grid_Content = 's-lc-rm-tg-cont'


# Seneca Username & Password
username_String = "TEST"
password_String = "TEST321321"

# Error Messages

Browser_Doesnt_Exist = "Browser doesn't exist ):"

# functions


def go_to_home():
    if 'browser' in globals():
        browser.get(Book_A_Study_Room_Link)
    else:
        raise Exception(Browser_Doesnt_Exist)


def Grab_Avaliability_Data(Campus):

    if 'browser' in globals():
        Selected_Campus = browser.find_element_by_id(Campus)
        Selected_Campus.click()

        table = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, Time_Grid_Content)))

        print("FOUND")

    else:
        raise Exception(Browser_Doesnt_Exist)


# Main code/logic
browser = webdriver.Chrome()
go_to_home()
Grab_Avaliability_Data(Newnham_Campus)

# browser.implicitly_wait(10)  # seconds


# def Agree_To_Terms():
#    Agree_Button = browser.find_element_by_id('agree_button')
#    Agree_Button.click()
#    return


# Seneca's Privacy and cookies agreement seems to pop up every time so we must set up something to accept it
