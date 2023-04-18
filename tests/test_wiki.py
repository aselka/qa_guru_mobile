import allure
from selene import have
from selene.support.shared import browser
from utils.app_locators import *


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Результат поиска не пустой')
def test_search_should_find_results():
    with allure.step('Переход на экран поиска и ввод искомого значения'):
        browser.element(search).click()
        browser.element(field_search).send_keys('QA GURU')
    with allure.step('Проверка результатов поиска'):
        browser.all(result_search).should(have.size_greater_than(0))


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Навигация по экранам приложения Wikipedia')
def test_skip_screens():
    with allure.step('Проверка стартового экрана'):
        browser.element(title).should(have.text("The Free Encyclopedia"))
        browser.element(btn_continue).click()
    with allure.step('Проверка перехода к второму экрана'):
        browser.element(title).should(have.text("New ways to explore"))
        browser.element(btn_continue).click()
    with allure.step('Проверка перехода к третьему экрану'):
        browser.element(title).should(have.exact_text("Reading lists with sync"))
        browser.element(btn_continue).click()
    with allure.step('Проверка перехода к четвертому экрана'):
        browser.element(title).should(have.text("Send anonymous data"))