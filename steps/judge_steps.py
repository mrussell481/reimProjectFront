from behave import given, when, then
import time


@given(u'The user is a manager')
def step_impl(context):
    context.driver.get('http://localhost:5000/')
    context.reim_main_page.user_field().send_keys("toughguy12")
    context.reim_main_page.pass_field().send_keys("0921q83n54v18746")
    context.reim_main_page.login_button().click()


@given(u'The manager is viewing a request')
def step_impl(context):
    context.reim_main_page.request_button_0().click()


@when(u'The manager types a comment')
def step_impl(context):
    context.reim_main_page.comment_box().send_keys("Working as intended!")


@when(u'The manager presses the Approve button')
def step_impl(context):
    context.reim_main_page.approve_button().click()


@then(u'A message notifies the manager that the request\'s Approval Status was updated')
def step_impl(context):
    time.sleep(1)
    response = context.reim_main_page.judge_response().text
    assert response == "Successfully updated request!"


@when(u'The manager presses the Deny button')
def step_impl(context):
    context.reim_main_page.deny_button().click()


@then(u'A message tells the manager that the request\'s Approval Status was updated')
def step_impl(context):
    time.sleep(1)
    response = context.reim_main_page.judge_response().text
    assert response == "Successfully updated request!"
