import json
import os
import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

use_step_matcher("re")

def wait_for_element_visibility_xpath(context, xpath):
    element = EC.visibility_of_element_located((By.XPATH, xpath))
    WebDriverWait(context.driver, 20).until(element)

def wait_for_element_visibility_id(context, id):
    element = EC.visibility_of_element_located((By.ID, id))
    WebDriverWait(context.driver, 20).until(element)

def waiting():
    sec = randint(2, 4)
    time.sleep(sec)
@given("GreenMile is running #2")
def step_impl(context):
    greenMile_service = requests.get('https://demo.greenmile.com')
    assert greenMile_service.status_code == 200

@when("a user searches for a pre existent form")
def step_impl(context):
    context.user = 'GM-Elizabeth'
    context.password = 'greenmile'
    context.form_description = 'Automated test'
    context.driver = webdriver.Chrome(executable_path='C:/Users/bethl/Documents/greenmile/testingGreenMile/features/steps/driver/chromedriver.exe')
    context.driver.get('https://demo.greenmile.com')

    wait_for_element_visibility_id(context, 'LoginBox')

    login_field = context.driver.find_element_by_id('j_username')
    login_field.send_keys(context.user)

    password_field = context.driver.find_element_by_id('j_password')
    password_field.send_keys(context.password)

    login_button = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/button')
    login_button.click()

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/a')

    maintance_dropdown = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/a')
    maintance_dropdown.click()

    smart_survey_item = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/ul/li[2]/a')
    smart_survey_item.click()

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[2]/form/div[3]/div[2]/div[1]/div[2]/div[2]/div[1]/input')

    description_search_field = context.driver.find_element_by_name('description')
    description_search_field.send_keys(context.form_description)

    magnifier_search_icon = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[2]/form/div[3]/div[2]/div[1]/div[2]/div[4]/input[1]')
    magnifier_search_icon.click()

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[2]/form/div[3]/div[2]/div[2]/div[5]/div[3]/div')
    waiting()


@then("GreenMile Service returns the one the user searched")
def step_impl(context):
    grid_elements = context.driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[2]/form/div[3]/div[2]/div[2]/div[5]/div[3]/div')
    element = False
    for i in grid_elements:
        if (context.form_description in i.text):
            element = True
            break
    assert element is True
    context.driver.quit()