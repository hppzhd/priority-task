@echo off
:: Включаем правильную кодировку для русских букв
chcp 65001 >nul

echo === ЭТАП 1: ЗАПУСК ТЕСТОВ (CI) ===
:: Используем команду py вместо python
py module.py

echo.
echo === ЭТАП 2: СБОРКА ОБРАЗА (CD) ===
:: Используем современную команду docker compose (без дефиса)
docker compose build

echo.
echo === ЭТАП 3: ИНТЕГРАЦИОННЫЙ ТЕСТ ===
docker compose up --abort-on-container-exit

echo.
echo === ПАЙПЛАЙН УСПЕШНО ЗАВЕРШЕН! ===
pause