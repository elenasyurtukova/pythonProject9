from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    """Класс реализации страницы логина"""
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        """Метод инициализации экземпляра класса страницы с помощью драйвера"""
        self.driver = driver

    def open(self):
        """Метод открытия сайта с заданным URL"""
        self.driver.get(self.URL)

    def enter_username(self, username):
        """Функция для ввода имени пользователя"""
        username.field = self.driver.find_element(By.ID, 'user-name')
        username.field.clear()
        username.field.send_keys(username)

    def enter_password(self, password):
        """Функция для ввода пароля"""
        password.field = self.driver.find_element(By.ID, 'password')
        password.field.clear()
        password.field.send_keys(password)

    def click_login(self):
        """Функция нажатия на кнопку логина (отправка формы)"""
        login_button = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        login_button.click()

    def get_current_url(self):
        """Метод, который возвращает текущую страницу для проверки успешности входа"""
        return self.driver.current_url

    def is_element_present(self, by, value):
        """Метод, который пробует найти элемент на странице с указанным методом(by) и значением(value)"""
        try:
            self.driver.find_element(by, value)
            return True
        except:
            return False