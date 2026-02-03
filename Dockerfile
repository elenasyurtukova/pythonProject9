# Используем официальный образ Python как базовый
FROM python:3.10-slim

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
  wget \
  gnupg \
  curl \
  unzip \
  && rm -rf /var/lib/apt/lists/*

# Установка Edge
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
  && install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ \
  && echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list \
  && apt-get update \
  && apt-get install -y microsoft-edge-stable \
  && rm -rf microsoft.gpg

# Копируем файл зависимостей
COPY requirements.txt .

# Проверяем на обновления pip
RUN pip install --upgrade pip

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade pytest allure-pytest

# Копируем исходный код
COPY . .

# Запускаем тесты
CMD ["pytest", "--alluredir=allure-results", "-v"]