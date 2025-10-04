import time
from behave import then
import allure
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@given("the user is on the login page")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-allow-origins=*")  # Important for newer Chrome versions

    context.driver = webdriver.Chrome(options=chrome_options)
    time.sleep(2)  # Give Flask time to stabilize

    context.driver.get("http://127.0.0.1:8000/login")

@when("the user enters valid username and password")
def step_impl(context):
    context.driver.find_element("name", "email").send_keys("admin@example.com")
    context.driver.find_element("name", "password").send_keys("admin123")
    context.driver.find_element("id", "login-button").click()

@then("the user should be redirected to the dashboard")
def step_impl(context):
    print("Current URL:", context.driver.current_url)
    print("Page Title:", context.driver.title)
    try:
        assert "Dashboard" in context.driver.title
    except AssertionError:
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Dashboard Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    finally:
        context.driver.quit()


@then("the user should see an error message")
def step_impl(context):
    try:
        body_text = context.driver.page_source
        assert "Invalid credentials" in body_text
    except AssertionError:
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Invalid Login Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    finally:
        context.driver.quit()
        

@when("the user enters invalid username and password")
def step_impl(context):
    context.driver.find_element("name", "email").send_keys("wrong@example.com")
    context.driver.find_element("name", "password").send_keys("wrongpass")
    context.driver.find_element("id", "login-button").click()
    time.sleep(2)
 



