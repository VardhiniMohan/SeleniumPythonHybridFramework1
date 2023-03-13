from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given(u'I Open the application using URL in browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.opencart.com/")
    context.driver.maximize_window()


@then(u'I should get website homepage')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Open Source Shopping Cart Solution")


@given(u'I click on feature option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[normalize-space()='Features']").click()


@then(u'I should get features page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Features")


@then(u'I close the driver')
def step_impl(context):
    context.driver.close()


@then(u'I should see all 6 options in header')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Features']")\
        .is_displayed()
    assert context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Demo']")\
        .is_displayed()
    assert context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Marketplace']")\
        .is_displayed()
    assert context.driver.find_element(By.XPATH,"//a[text()='Blog']").is_displayed()
    assert context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Download']")\
        .is_displayed()
    assert context.driver.find_element(By.XPATH,"//li[@class='dropdown']/a").is_displayed()


@then(u'I should see account and logout options in header')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//a[@class='btn btn-link navbar-btn']").is_displayed()
    assert context.driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']").is_displayed()


@when(u'I click on feature option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[text()='Features']").click()


@then(u'I click on demo option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Demo']").click()


@then(u'I should get demo page')
def step_impl(context):
    assert context.driver.title == "OpenCart - Demo"


@then(u'I click on marketplace option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Marketplace']").click()


@then(u'I should get marketplace page')
def step_impl(context):
    assert context.driver.title == "Opencart extensions"


@then(u'I click on blog option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Blog']").click()


@then(u'I should get blog page')
def step_impl(context):
    assert context.driver.title == "OpenCart - Blog"


@then(u'I click on download option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='nav navbar-nav']//a[text()='Download']").click()


@then(u'I should get download page')
def step_impl(context):
    assert context.driver.title == "OpenCart - Downloads"


@then(u'I click on resource-developer option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@class='dropdown']/a").click()
    context.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu']/li[9]/a").click()


@then(u'I should get resource-developer page')
def step_impl(context):
    assert context.driver.title == "OpenCart Documentation"


@when(u'I click on Account option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='btn btn-link navbar-btn']").click()


@then(u'I click on logout option')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']").click()


@then(u'I should get to logout page')
def step_impl(context):
    assert context.driver.title == "OpenCart - Open Source Shopping Cart Solution"


@then(u'I should observe correct UI details in entire header area')
def step_impl(context):
    context.element1 = context.driver.find_element(By.ID, "navbar-collapse-header")
    assert context.element1.value_of_css_property("font-size").__eq__("16px")
    assert context.element1.value_of_css_property("line-height").__eq__("25.6px")


@then(u'I should observe correct UI details in logo area')
def step_impl(context):
    context.element2 = context.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[1]/a/img")
    assert context.element2.value_of_css_property("margin-top").__eq__("21px")
    assert context.element2.value_of_css_property("height").__eq__("36px")

