import allure
import pytest
from selene import have
from selene.support.shared import browser
from utils.app_locators import *
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture()
def skip():
    with allure.step('Skipping initial screens'):
        browser.element(btn_skip).click()


def test_search_should_find_results():
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).send_keys('BrowserStack')
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.size_greater_than(0))


def test_open_page():
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).send_keys('api test')
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()
    browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('An error occurred'))
