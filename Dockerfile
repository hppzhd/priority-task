# 1. Берем официальный образ Python
FROM python:3.9-slim

# 2. Создаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Копируем наши скрипты (сервер и логику)
COPY app.py .
COPY module.py .

# 5. Команда, которая запустит сервер при старте контейнера
CMD ["python", "app.py"]