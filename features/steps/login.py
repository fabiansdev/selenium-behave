from selenium.webdriver.common.by import By
from behave import given, then
import time


@given('Im opening website')
def step_impl(context):
    context.home_page.navigate("https://8tracks.com/")

@then('Im click log in button')
def step_impl(context):
    context.home_page.click_element(context.home_page.LOGIN_BTN)
    time.sleep(5)

@then("Im typing my username")
def step_impl(context):
    context.home_page.fill('myusername', context.home_page.USERNAME_FIELD)
    time.sleep(5)

@then("Im typing my password")
def step_impl(context):
    context.home_page.fill('mypassword', context.home_page.PASSWD_FIELD)
    time.sleep(5)

@then('Im submit log in')
def step_impl(context):
    context.home_page.click_element(context.home_page.SUBMIT_BUTTON)
    time.sleep(5)
