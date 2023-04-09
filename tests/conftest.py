import allure
import allure_commons
import pytest
from selene.support.shared import browser
from selene import support
from appium import webdriver
import config
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def app():
    browser.config.timeout = config.settings.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    yield

    attach.add_video(browser)
    attach.add_screenshot(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def add_labels():
    allure.dynamic.label('owner', 'asel')