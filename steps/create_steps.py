from behave import given, when, then
import time


@given(u'The user is a member')
def step_impl(context):
    context.driver.get('http://localhost:5000/')
    context.reim_main_page.user_field().send_keys("realrocky46")
    context.reim_main_page.pass_field().send_keys("jkcbn43857qo")
    context.reim_main_page.login_button().click()


@when(u'The member presses the Submit New Bug button')
def step_impl(context):
    time.sleep(1)
    context.reim_main_page.new_request_button().click()


@then(u'The New Request page is loaded')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "New Bug"


@when(u'The member enters a Bug Name')
def step_impl(context):
    context.reim_main_page.bug_name_field().send_keys("Selenium Bug")


@when(u'The member enters a Bug Description')
def step_impl(context):
    context.reim_main_page.bug_desc_field().send_keys("Selenium can submit bugs all by itself")


@when(u'the member presses the Submit button')
def step_impl(context):
    context.reim_main_page.submit_request_button().click()


@then(u'A message notifies the member that they successfully uploaded a new bug')
def step_impl(context):
    time.sleep(2)
    response = context.reim_main_page.server_response().text
    assert response == "Successfully uploaded new bug!"
