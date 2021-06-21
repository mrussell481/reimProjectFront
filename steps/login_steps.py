from behave import given, when, then
import time


@given(u'The member is on the log in page')
def step_impl(context):
    context.driver.get('http://localhost:5000/')


@when(u'A member username is entered')
def step_impl(context):
    context.reim_main_page.user_field().send_keys("realrocky46")


@when(u'A member password is entered')
def step_impl(context):
    context.reim_main_page.pass_field().send_keys("jkcbn43857qo")


@when(u'The Login button is pressed')
def step_impl(context):
    context.reim_main_page.login_button().click()


@then(u'The main request page is loaded')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Main Page"


@given(u'The manager is on the log in page')
def step_impl(context):
    context.driver.get('http://localhost:5000/')


@when(u'A manager username is entered')
def step_impl(context):
    context.reim_main_page.user_field().send_keys("toughguy12")


@when(u'A manager password is entered')
def step_impl(context):
    context.reim_main_page.pass_field().send_keys("0921q83n54v18746")
