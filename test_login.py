import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
import allure

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

@allure.suite('Login Tests Suite')
class TestLogin:
    """Класс тестирования логина с помощью фикстуры"""
    @pytest.mark.parametrize("username, password, expected_url, should_fail",
                             [
        ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html', False), # успешный логин
        ('standard_user', 'wrong_password', 'https://www.saucedemo.com/', True), # неверный пароль
        ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/', True), # заблокированный пользователь
        ('', '', 'https://www.saucedemo.com/', True), # пустые поля логина и пароля
        ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html', False) # Performance user
                              ]
                             )
    def test_login(self, driver, username, password, expected_url, should_fail):
        """Функция тестирования логина"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        time.sleep(2) # Ждем загрузки страницы

        current_url = login_page.get_current_url()
        if should_fail:
            assert current_url == 'https://www.saucedemo.com/', f'Expected failed login page but got {current_url}'
            assert login_page.is_element_present(By.CSS_SELECTOR, '.error-message-container') # Проверяем наличие сообщения об ошибке
        else:
            assert current_url == expected_url, f'Expected {expected_url} but got {current_url}'
            assert login_page.is_element_present(By.CLASS_NAME, 'inventory_list') # Проверяем, что список товаров загружен
