import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I should observe correct font size and line height in content section')
def step_impl(context):
    element = context.driver.find_element(By.ID, "common-home")
    assert element.value_of_css_property("font-size").__eq__("16px")
    assert element.value_of_css_property("line-height").__eq__("25.6px")


@then(u'I should observe resizing of contents upon resizing screen')
def step_impl(context):
    def changing(x, y):
        context.driver.set_window_size(x, y)
        # wait for the page to load
        #time.sleep(3)
        element = context.driver.find_element(By.XPATH, "//div[@id='common-home']")
        # get the position and size of the image element
        location = element.location
        size = element.size
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


@given(u'I save this as parent window')
def step_impl(context):
    context.parent = context.driver.current_window_handle


@then(u'I should see section 2 in content section')
def step_impl(context):
    assert context.driver.find_element(By.ID, "business").is_displayed()


@then(u'I click on british red cross logo')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "//img[@src='application/view/image/home/brand/british-red-cross.png']").click()
    time.sleep(5)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get british red cross website')
def step_impl(context):
    assert context.driver.title == "Shop charity gifts | British Red Cross Gift Shop"
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on BJPenn logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/bjpenn.com.png']").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get BJPenn website')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://shop.bjpenn.com/")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on Concordia College logo')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                "//img[@src='application/view/image/home/brand/concordia-college.png']").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get Concordia College website')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://shop.concordia-ny.edu/")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on FX Creations logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/fx-creation.png']").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get FX Creations website')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://fxcreations.com/")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on HKU logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/hkuvcg.png']").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get HKU website')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://www.visitorcentre.hku.hk/")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I should see section 3 in content section')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[@id='marketplace']").is_displayed()


@then(u'I click on Visit Marketplace option in section 3')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Visit Marketplace']").click()


@then(u'I should see section 4 in content section')
def step_impl(context):
    assert context.driver.find_element(By.ID, "extension").is_displayed()


@then(u'I click on Visit All option in section 3')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Visit All']").click()


@then(u'I should see section 5 in content section')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[@id='support']").is_displayed()


@then(u'I should see correct padding and text alignment')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//div[@class='page-header']//div[@class='row']")
    assert element.value_of_css_property("padding-top").__eq__("10px")
    assert element.value_of_css_property("padding-bottom").__eq__("20px")
    assert element.value_of_css_property("text-align").__eq__("center")


@then(u'I should see section 6 in content section')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[7]").is_displayed()


@then(u'I click on Community support- learn more option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Learn More'][1]").click()
    time.sleep(5)


@then(u'I should get Community forum page')
def step_impl(context):
    context.driver.title.__eq__("OpenCart Community - Index page")
    context.driver.back()


@then(u'I click on Dedicated support- learn more option')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='support']/div[2]/div[2]/p[2]/a[1]").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get Dedicated support page')
def step_impl(context):
    context.driver.title.__eq__("OpenCart Enterprise Services")


@then(u'I should see section 7 in content section')
def step_impl(context):
    assert context.driver.find_element(By.ID, "press").is_displayed()


@then(u'I click on Forbes logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='press']/div[1]/div[1]/div[2]/ul/li/a/img").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get forbes page')
def step_impl(context):
    assert context.driver.title.__eq__("3 Steps To Launch Your First eCommerce Website")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on Paypal logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@title='PayPal']").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get paypal page')
def step_impl(context):
    assert context.driver.title.__eq__("PayPal for Business | Merchant Services | PayPal UK")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on BBC logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='press']/div[1]/div[1]/div[2]/ul/li[3]/a/img").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get BBC page')
def step_impl(context):
    assert context.driver.title.__eq__("Tech tools make selling to the world child's play - BBC News")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on South China Morning Post logo')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='press']/div[1]/div[1]/div[2]/ul/li[4]/a/img").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get South China Morning Post  page')
def step_impl(context):
    assert context.driver.title.__eq__("A Business Mind: Daniel Kerr, founder of OpenCart | South China Morning Post")
    context.driver.close()
    context.driver.switch_to.window(context.parent)

