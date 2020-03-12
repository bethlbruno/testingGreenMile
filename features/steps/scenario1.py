import json
import os
import requests
from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

use_step_matcher("re")


def loading_spinner(driver):
    spinner = EC.visibility_of_element_located(
        (By.ID, 'spinner'))
    WebDriverWait(driver, 10).until(spinner)

    while True:
        try:
            driver.find_element_by_id('spinner')
        except NoSuchElementException:
            break


def waiting():
    sec = randint(5, 7)
    time.sleep(sec)


@given("GreenMile is running")
def step_impl(context):
    greenMile_service = requests.get('https://demo.greenmile.com')
    assert greenMile_service.status_code == 200

@when("a User fill the Description, Organization, application rules and save the form")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C:/Users/bethl/Documents/greenmile/testingGreenMile/features/steps/driver/chromedriver.exe')
    context.driver.get('https://demo.greenmile.com')

    login_box = EC.visibility_of_element_located((By.ID, 'LoginBox'))
    WebDriverWait(context.driver, 20).until(login_box)

    login_field = context.driver.find_element_by_id('j_username')
    login_field.send_keys('GM-Elizabeth')

    password_field = context.driver.find_element_by_id('j_password')
    password_field.send_keys('greenmile')

    login_button = context.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/button')
    login_button.click()

    menu_bar = EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/a'))
    WebDriverWait(context.driver, 20).until(menu_bar)

    maintance_dropdown = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/a')
    maintance_dropdown.click()
    smart_survey_item = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/header/div/nav/ul/li[1]/ul/li[2]/a')
    smart_survey_item.click()

    new_form_bar = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[2]/div'))
    WebDriverWait(context.driver, 20).until(new_form_bar)

    # new_form_button = context.driver.find_element_by_id('Survey_btn_novo')
    # new_form_button.click()
    #
    # description_form = EC.visibility_of_element_located((By.ID, 'Survey_description'))
    # WebDriverWait(context.driver, 20).until((description_form))
    #
    # description_field = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[2]/input')
    # description_field.send_keys('automated test')
    #
    # magnifier_icon = context.driver.find_element_by_class_name('lookupSearchButton')
    # magnifier_icon.click()
    #
    # organization_search_box = EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[4]/div[4]/div[3]/div/div/div[1]'))
    # WebDriverWait(context.driver, 20).until(organization_search_box)
    #
    # organization_GM_Elizabeth = context.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div/div[3]/div/div[3]/form/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[4]/div[4]/div[3]/div/div/div[1]')
    # organization_GM_Elizabeth.click()
    #
    # add_application_rules_button = context.driver.find_element_by_id('SurveyApplyRulesOpenModal')
    # add_application_rules_button.click()
    #
    # save_application_rules_button = context.driver.find_element_by_id('LinkFormSaveButton')
    # save_application_rules_button.click()
    #
    # delete_section_icon = context.driver.find_element_by_class_name('destroyGroup')
    # delete_section_icon.click()
    #
    # confirm_selection_alert = context.driver.switch_to.alert
    # confirm_selection_alert.accept()
    #
    # save_form_button = context.driver.find_element_by_id('Survey_btn_new_save')
    # save_form_button.click()
    time.sleep(2)
    pass

@then("GreenMile Service returns the updated form in the grid")
def step_impl(context):
    test = context.driver.find_elements_by_class_name('grid-canvas grid-canvas-top grid-canvas-right')
    for i in test:
        print(str(i))
    pass

