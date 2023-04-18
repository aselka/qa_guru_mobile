import pytest
import allure
from selene import have
from selene.support.shared import browser
from utils.app_locators import *


@pytest.fixture()
def skip():
    with allure.step('Пропуск стартовых экранов'):
        browser.element(btn_skip).click()


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Результат поиска не пустой')
def test_search_should_find_results(skip):
    with allure.step('Переход на экран поиска и ввод искомого значения'):
        browser.element(search).click()
        browser.element(field_search).send_keys('QA GURU')
    with allure.step('Проверка результатов поиска'):
        browser.all(result_search).should(have.size_greater_than(0))


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Пустой поиск')
def test_empty_search(skip):
    with allure.step('Поиск пустого значения'):
        browser.element(search).click()
        browser.element(field_search).send_keys('')

    with allure.step('Проверка результатов поиска'):
        browser.all(result_search).should(have.size(0))


@allure.label('owner', 'bisengalieva')
@allure.feature('Тесты Wikipedia')
@allure.title('Переход на главную по кнопке "skip"')
def test_skip_main_screens(skip):
    with allure.step('Проверка отображения главного экрана'):
        browser.element(ann_main_screen).should(have.text('Customize your Explore feed'))
