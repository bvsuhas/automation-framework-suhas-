import time
from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage

@given('the user is on the login page')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://practicetestautomation.com/practice-test-login/")
    context.login_page = LoginPage(context.driver)

@when('the user enters valid username and password')
def step_enter_credentials(context):
    context.login_page.enter_username("student")       # ✅ correct username
    context.login_page.enter_password("Password123")   # ✅ correct password
    context.login_page.click_login()

@then('the user should be redirected to the dashboard')
def step_verify_dashboard(context):
    assert "Logged In Successfully" in context.driver.page_source
    time.sleep(10)
    context.driver.quit()

