import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'I should see Opencart options in footer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='row']//div[1]//section[1]").is_displayed()


@then(u'I click on Features option under opencart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li/a").click()


@then(u'I click on Showcase option under opencart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li[2]/a").click()


@then(u'I should get Resource-showcase page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Showcase")


@then(u'I click on Demo option under opencart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li[3]/a").click()


@then(u'I click on Download option under opencart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li[4]/a").click()


@then(u'I click on Marketplace option under opencart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li[5]/a").click()


@then(u'I click on Login option under opencart')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li[6]/a").click()


@then(u'I should see Company options in footer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='row']//div[2]//section[1]").is_displayed()


@then(u'I click on Contact Us option under Company')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[normalize-space()='Contact Us']").click()


@then(u'I should get Contact page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Contact")


@then(u'I click on Extension Advertising option under Company')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[normalize-space()='Extension Advertising']").click()


@then(u'I should get Advertising page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Advertising")


@then(u'I click on Marketplace Advertising option under Company')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[normalize-space()='Marketplace Advertising']").click()


@then(u'I click on About Us option under Company')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[normalize-space()='About Us']").click()


@then(u'I should get Company page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Company")


@then(u'I click on Terms & Conditions option under Company')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Terms & Conditions']").click()


@then(u'I should get Policy page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Policy")


@then(u'I click on Extension Developer option under Company')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a[text()='Extension Developer']").click()


@then(u'I should get Extension Developer page')
def step_impl(context):
    assert context.driver.title.__eq__("How to be a seller of Opencart?")


@then(u'I should see Support options in footer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[3]//section[1]").is_displayed()


@then(u'I click on Community Forum option under Support')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,"Community Forum").click()


@then(u'I click on Dedicated Support option under Support')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,"Dedicated Support").click()


@then(u'I should get Support page')
def step_impl(context):
    context.driver.title.__eq__("OpenCart Enterprise Services")
    context.driver.back()


@then(u'I click on OpenCart Partners option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='OpenCart Partners']").click()


@then(u'I should get Resources-Partners page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Partners")


@then(u'I click on Marketplace Support option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='Marketplace Support']").click()


@then(u'I click on Migrate to OpenCart option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='Migrate to OpenCart']").click()


@then(u'I should get Migrate to OpenCart page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart - Cart2Cart Migration")


@then(u'I should see resources options in footer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[4]//section[1]").is_displayed()


@then(u'I click on OpenCart Blog option under Support')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,"OpenCart Blog").click()


@then(u'I click on OpenCart Documentation option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='OpenCart Documentation']").click()


@then(u'I should get resource-Documentation page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart Documentation")


@then(u'I click on OpenCart Books option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='OpenCart Books']").click()


@then(u'I should get resource-Books page')
def step_impl(context):
    assert context.driver.title.__eq__("OpenCart Documentation")


@then(u'I click on GitHub Bug Tracker option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//body[1]/footer[1]/div[1]/div[1]/div[4]/section[1]/ul[1]/li[4]/a").click()


@then(u'I should get resource-GitHub Bug Tracker page')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://github.com/opencart/opencart/issues")
    context.driver.back()


@then(u'I click on Developer option under Support')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='Developer']").click()


@then(u'I should see Newsletter section in footer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//section[@id='newsletter']").is_displayed()


@then(u'I should see Newsletter statement under Newsletter')
def step_impl(context):
    words = context.driver.find_element(By.XPATH, "//section[@id='newsletter']//p").text
    assert words.__eq__("Subscribe to our newsletters and stay informed of new releases and other OpenCart events.")


@then(u'I should see correct placeholder text in input field')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//section[@id='newsletter']//div/input").get_attribute("placeholder").__eq__("Enter your email address")


@then(u'I should see Social section in footer')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@id='social']/ul").is_displayed()


@then(u'I click on Facebook Marketing Partner option under Social')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='social']/ul/li/a/img").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get Meta-partners page')
def step_impl(context):
    assert context.driver.title.__eq__("Commerce | partner badge")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on LinkedIn option under Social')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='social']/ul/li[2]/a").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get LinkedIn page')
def step_impl(context):
    assert context.driver.title.__eq__("LinkedIn Login, Sign in | LinkedIn")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on Facebook option under Social')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='social']/ul/li[3]/a").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get Facebook page')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://www.facebook.com/opencart/?ref=aymt_homepage_panel")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@then(u'I click on Twitter option under Social')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='social']/ul/li[4]/a").click()
    context.driver.switch_to.window(context.driver.window_handles[1])


@then(u'I should get Twitter page')
def step_impl(context):
    assert context.driver.current_url.__eq__("https://twitter.com/opencart")
    context.driver.close()
    context.driver.switch_to.window(context.parent)


@when(u'I enter email in newsletter input field')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//section[@id='newsletter']/div/input").send_keys("vardhinivm11@gmail.com")


@when(u'I click on arrow')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//section[@id='newsletter']/div/div/button/i").click()
    time.sleep(5)


@then(u'I should see "Sign-up for Newsletter" form pop-up')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//div[@class='modal-content']").is_displayed()


@then(u'I should observe correct padding, margin, font size and line height in content section')
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//body//footer")
    assert element.value_of_css_property("padding").__eq__("60px 0px")
    assert element.value_of_css_property("margin").__eq__("0px")
    assert element.value_of_css_property("font-size").__eq__("14px")
    assert element.value_of_css_property("line-height").__eq__("22.4px")

