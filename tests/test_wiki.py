import pytest
import allure
from selene import have
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture()
def skip():
    with allure.step('Пропуск стартовых экранов'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Результат поиска не пустой')
def test_search_should_find_results():
    with allure.step('Переход на экран поиска и ввод искомого значения'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).send_keys('QA GURU')
    with allure.step('Проверка результатов поиска'):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.size_greater_than(0))


@allure.label('owner', 'bisengalieva')
@allure.title('Test empty search')
def test_empty_search():
    with allure.step('Поиск пустого значения'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).send_keys('')

    with allure.step('Проверка результатов поиска'):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.size_greater_than(0))


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Переход на главную по кнопке "skip"')
def test_skip_main_screens(skip):
    with allure.step('Проверка отображения главного экрана'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')).should(have.text('Customize your Explore feed'))
