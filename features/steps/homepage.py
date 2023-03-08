import datetime
import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given(u'I navigate to register page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']").click()


@when(u'I enter mandatory details in register page')
def step_impl(context):
    context.driver.find_element(By.ID,"input-username").send_keys("username"+datetime.datetime.now().strftime("%H_%M_%S"))
    context.driver.find_element(By.ID,"input-firstname").send_keys("user12")
    context.driver.find_element(By.ID,"input-lastname").send_keys("name12")
    random_mail = "vardhinivm" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "@gmail.com"
    context.driver.find_element(By.ID,"input-email").send_keys(random_mail)
    dropdown1 = context.driver.find_element(By.ID, "input-country")
    dropdown1.click()
    select = Select(dropdown1)
    select.select_by_visible_text("India")
    context.driver.find_element(By.ID,"input-password").send_keys("12345")
    time.sleep(5)


@when(u'I click on register button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[text()='Register']").click()
    context.driver.find_element(By.XPATH,"//a[text()='Continue']").click()


@then(u'I should get to account page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//p[text()='Welcome to OpenCart!']").is_displayed()


@given(u'I navigate to login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='btn btn-link navbar-btn']").click()


@when(u'I enter mandatory details in login page')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("vardhinivm11@gmail.com")
    context.driver.find_element(By.ID,"input-password").send_keys("12345")


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[text()='Login']").click()


@when(u'I enter keys in send keys field')
def step_impl(context):
    context.driver.find_element(By.ID,"input-pin").send_keys("2491")


@when(u'I click continue')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[text()='Continue']").click()


@given(u'I successfully login into the application')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("vardhinivm11@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.XPATH, "//button[text()='Login']").click()
    context.driver.find_element(By.ID, "input-pin").send_keys("2491")
    context.driver.find_element(By.XPATH, "//button[text()='Continue']").click()


@when(u'I click on the logo')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//img[@title='OpenCart - Your Account']").click()


@when(u'I click on the logo again')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//img[@title='OpenCart - Open Source Shopping Cart Solution']").click()


@then(u'I should get to home page')
def step_impl(context):
    assert context.driver.title == "OpenCart - Open Source Shopping Cart Solution"


@then(u'I should get correct website URL and page title in home page')
def step_impl(context):
    assert context.driver.title == "OpenCart - Open Source Shopping Cart Solution"
    assert context.driver.current_url == "https://www.opencart.com/index.php?route=common/home"


@then(u'I should get to login page')
def step_impl(context):
    context.driver.title.__eq__("Opencart - Account Login")
