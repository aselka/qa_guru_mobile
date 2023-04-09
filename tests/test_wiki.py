import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from utils.app_locators import *


@pytest.fixture()
def skip():
    with allure.step('Skipping initial screens'):
        browser.element(btn_skip).click()


@allure.title('Navigation in the Wikipedia app')
def test_skip_screens(add_labels):
    with allure.step('Checking the start screen'):
        browser.element(title).should(have.text('The Free Encyclopedia'))
        browser.element(btn_continue).click()
    with allure.step('"Continue" page one'):
        browser.element(title).should(have.text('New ways to explore'))
        browser.element(btn_continue).click()
    with allure.step('"Continue" page two'):
        browser.element(title).should(have.exact_text('Reading lists with sync'))
        browser.element(btn_continue).click()
    with allure.step('"Continue" page three'):
        browser.element(title).should(have.text('Send anonymous data'))


def test_main_screen_displayed(add_labels, skip):
    with allure.step('Verify main screen is displayed'):
        browser.element(ann_main_screen).should(have.text('Customize your Explore feed'))


def test_search(add_labels, skip):
    with allure.step('Navigate to the search screen and enter the search query'):
        browser.element(search).click()
        browser.element(field_search).type('QA.GURU')
    with allure.step(' Verifying search results'):
        browser.all(result_search).should(have.size_greater_than(0))


def test_text_error(add_labels, skip):
    with allure.step('Navigate to the login screen'):
        browser.element(btn_menu).click()
        browser.element(menu_item_login).click()
    with allure.step('Enter invalid value into "User" field'):
        browser.element(field_username).type('***')
    with allure.step('Check the error message for invalid input'):
        browser.element(text_error).should(
            have.exact_text('The user name "***" is not available. Please choose a different name.'))


def test_empty_page(add_labels, skip):
    with allure.step('Navigate to the saved pages screen'):
        browser.element(widget_saved).click()
        browser.element(btn_negative).click()
    with allure.step('Verifying the text on empty screen'):
        browser.element(empty_list).should(have.exact_text('No saved pages yet'))
