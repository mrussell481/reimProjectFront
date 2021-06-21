# Features do the following:
# Login tests both manager and member logins
# Create makes two new requests as a member
# Judge approves one request and denies the other as a manager
# View selects three different requests as a manager

from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from poms.reim_main_page import ReimMainPage


def before_all(context: Context):
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    context.driver = webdriver.Firefox(firefox_binary=binary,
                                       executable_path="C:\\Users\\mrmas_d2t5g6y\\Desktop\\Programming\\Drivers"
                                                       "\\geckodriver.exe")
    context.reim_main_page = ReimMainPage(context.driver)
    context.driver.implicitly_wait(3)
    print("Starting front-end testing...")


def after_all(context):
    print("Testing complete.")
    context.driver.quit()