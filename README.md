# Автоматизация тестирования логина на сайте SauceDemo

## Описание проекта
Проект содержит автоматизированные тесты для проверки функционала авторизации на сайте 
https://www.saucedemo.com/ для браузера Microsoft Edge

## Тестовые сценарии
1. Успешный логин (standard_user / secret_sauce)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин пользователем performance_glitch_user

## Запуск тестов локально

### Предварительные требования
- Python 3.10 или выше
- pip (менеджер пакетов Python)
- установленный браузер Microsoft Edge

### Клонируйте репозиторий:
```git clone git@github.com:elenasyurtukova/pythonProject9.git```

### Установите зависимости
pip install -r requirements.txt

### Установите Docker для контейнеризации проекта:
Для работы с Docker если вы используете Windows/macOS установите на ваш 
компьютер приложение Docker Desktop  https://www.docker.com/products/docker-desktop,
а если - Linux можно установить Docker на примере Ubuntu.
Официальная инструкция по установке находится по ссылке: 
https://docs.docker.com/engine/install/ubuntu/.

### Установите Allure:
#### Для Windows:
1. Скачайте Allure с [официального сайта](https://github.com/allure-framework/allure2/releases)
2. Распакуйте архив
3. Добавьте путь к `bin` в переменную PATH

#### Для Linux:
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure

#### Для Mac:
brew install allure

### Запустите тесты с сохранением результатов в папку allure-results
pytest --alluredir=allure-results -v

### Запустите тесты в Docker
- сборка образа: docker build -t saucedemo-tests .
- запуск тестов: docker run --rm saucedemo-tests