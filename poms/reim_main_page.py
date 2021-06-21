from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class ReimMainPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def user_field(self):
        element: WebElement = self.driver.find_element_by_id("user_field")
        return element

    def pass_field(self):
        element: WebElement = self.driver.find_element_by_id("pass_field")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element_by_id("login_button")
        return element

    def request_button_0(self):
        element: WebElement = self.driver.find_element_by_id("request_button_0")
        return element

    def new_request_button(self):
        element: WebElement = self.driver.find_element_by_id("new_request_button")
        return element

    def bug_name_field(self):
        element: WebElement = self.driver.find_element_by_id("bug_name_field")
        return element

    def bug_desc_field(self):
        element: WebElement = self.driver.find_element_by_id("bug_desc_field")
        return element

    def submit_request_button(self):
        element: WebElement = self.driver.find_element_by_id("submit_request_button")
        return element

    def server_response(self):
        element: WebElement = self.driver.find_element_by_id("server_response")
        return element

    def comment_box(self):
        element: WebElement = self.driver.find_element_by_id("comment_box")
        return element

    def approve_button(self):
        element: WebElement = self.driver.find_element_by_id("approve_button")
        return element

    def deny_button(self):
        element: WebElement = self.driver.find_element_by_id("deny_button")
        return element

    def judge_response(self):
        element: WebElement = self.driver.find_element_by_id("judge_response")
        return element


