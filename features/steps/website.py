from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I Open the application using URL in browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.opencart.com/")
    context.driver.maximize_window()


@then(u'I should get website homepage')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Open Source Shopping Cart Solution")


@given(u'I Open the application using URL in edge browser')
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.get("https://www.opencart.com/")
    context.driver.maximize_window()


@given(u'I click on feature option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[normalize-space()='Features']").click()


@then(u'I should get features page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Features")


@then(u'I close the driver')
def step_impl(context):
    context.driver.close()

