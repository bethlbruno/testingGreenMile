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
from selenium.webdriver.remote.webelement import WebElement

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

use_step_matcher("re")

def wait_for_element_visibility_xpath(context, xpath):
    element = EC.visibility_of_element_located((By.XPATH, xpath))
    WebDriverWait(context.driver, 10).until(element)

def wait_for_element_visibility_id(context, id):
    element = EC.visibility_of_element_located((By.ID, id))
    WebDriverWait(context.driver, 10).until(element)

def waiting():
    sec = randint(2, 4)
    time.sleep(sec)
@given("GreenMile is running #1")
def step_impl(context):
    greenMile_service = requests.get('https://demo.greenmile.com')
    assert greenMile_service.status_code == 200

@when("a User fill the Description, Organization, application rules and save the form")
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

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/header/div/nav/ul')

    maintance_dropdown = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/a')
    maintance_dropdown.click()

    smart_survey_item = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/ul/li[2]/a')
    smart_survey_item.click()

    new_form_bar = EC.element_to_be_clickable((By.ID, 'Survey_btn_novo'))
    WebDriverWait(context.driver, 10).until(new_form_bar)

    new_form_button = context.driver.find_element_by_id('Survey_btn_novo')
    new_form_button.click()

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[2]/input')

    description_field = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[2]/input')
    description_field.send_keys(context.form_description)

    magnifier_icon = context.driver.find_element_by_class_name('lookupSearchButton')
    magnifier_icon.click()

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[4]/div[4]/div[3]/div/div/div[1]')

    organization_GM_Elizabeth = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[4]/div[4]/div[3]/div/div/div[1]')
    organization_GM_Elizabeth.click()

    add_application_rules_button = context.driver.find_element_by_id('SurveyApplyRulesOpenModal')
    add_application_rules_button.click()

    save_application_rules_button = context.driver.find_element_by_id('LinkFormSaveButton')
    save_application_rules_button.click()

    delete_section_icon = context.driver.find_element_by_class_name('destroyGroup')
    delete_section_icon.click()

    confirm_selection_alert = context.driver.switch_to.alert
    confirm_selection_alert.accept()

    save_form_button = context.driver.find_element_by_id('Survey_btn_new_save')
    save_form_button.click()

    wait_for_element_visibility_xpath(context, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[2]/div[5]/div[3]/div')
    waiting()


@then("GreenMile Service returns the updated form in the grid")
def step_impl(context):
    grid_elements = context.driver.find_elements_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[2]/form/div[3]/div[2]/div[2]/div[5]/div[3]/div')
    element = False
    for i in grid_elements:
        if (context.form_description in i.text):
            element = True
            break
    assert element is True
    context.driver.quit()

