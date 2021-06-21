from behave import when, then
import time


@when(u'The user clicks on the Open button next to a request')
def step_impl(context):
    time.sleep(1)
    context.reim_main_page.request_button_0().click()


@then(u'The page for that request is loaded')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Selenium Bug"
