from behave import *
from selenium import webdriver
from time import sleep


@given(u'Browser Launch')
def Browser(context):
    #context.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    # raise NotImplementedError(u'STEP: Given Browser Launch')
    context.driver=webdriver.Chrome()
    # driver = webdriver.Firefox()
    sleep(5)


@when(u'Amazon Login Page')
def Open_Login(context):
    # raise NotImplementedError(u'STEP: When Yahoo Login Page')
    context.driver.get("https://www.amazon.co.uk/")
    sleep(5)



@then(u'Verify logo')
#Verify the Logo
def Verify_Logo(context):
    # raise NotImplementedError(u'STEP: Then Verify logo')
    context.driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in')]").click()
    # assert status is True
    sleep(5)


@then(u'Browser Close')
def Close_Browser(context):
    # raise NotImplementedError(u'STEP: Then Browser Close')
    context.driver.close()
    sleep(5)

# Looking at Amzon Logo in UK Server
