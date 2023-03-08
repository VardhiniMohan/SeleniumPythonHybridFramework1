import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I should see the image in hero section within viewport')
def step_impl(context):
    image = context.driver.find_element(By.XPATH, "//div[@class='device hidden-xs hidden-sm']")
    # get the position and size of the image element
    location = image.location
    size = image.size
    # check if the image is within the viewport of the browser window
    viewport_height = context.driver.execute_script("return window.innerHeight;")
    assert 0 <= location['y'] <= viewport_height


@then(u'I should see correct font size and padding')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//div[@id='hero']/div/div/div")
    assert element.value_of_css_property("font-size").__eq__("16px")
    assert element.value_of_css_property("padding-left").__eq__("15px")
    assert element.value_of_css_property("padding-right").__eq__("15px")


@then(u'I should observe resizing of image upon resizing screen')
def step_impl(context):
    def changing(x, y):
        context.driver.set_window_size(x, y)
        # wait for the page to load
        time.sleep(3)
        image = context.driver.find_element(By.XPATH, "//div[@class='device hidden-xs hidden-sm']")
        # get the position and size of the image element
        location = image.location
        size = image.size

        # check if the image is within the viewport of the browser window
        viewport_height = context.driver.execute_script("return window.innerHeight;")
        assert 0 <= location['y'] <= viewport_height

    changing(100, 500)
    changing(200, 700)
    changing(300, 500)
    changing(400, 400)
    changing(500, 900)
    changing(600, 400)
    changing(800, 600)
    changing(1000, 500)


@when(u'I click Free Download option in hero section')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Free Download']").click()


@then(u'I navigate to home page from download page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='navbar-header']").click()


@then(u'I click view demo option in hero section')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='View Demo']").click()

