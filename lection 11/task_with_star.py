# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

download_folder = os.path.join(os.getcwd())
prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": download_folder,
         "directory_upgrade": True, "safebrowsing.enabled": True}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options)

try:
    # Перейти на  https://sbis.ru/
    driver.get('https://sbis.ru/')
    sleep(3)

    # В Footer'e найти "Скачать СБИС"
    link = driver.find_element(By.CSS_SELECTOR, '[href="/download"]')
    link.click()

    # Скачать СБИС Плагин для вашей ОС в папку с данным тестом
    file = driver.find_element(By.CSS_SELECTOR, '.sbis_ru-DownloadNew-loadLink__link.js-link')
    file.click()

    # Убедиться, что плагин скачался
    file_name = 'sbisplugin-setup-web.exe'
    for i in range(30):
        sleep(1)
        if file_name in os.listdir(download_folder):
            break

    # Вывести на печать размер скачанного файла в мегабайтах
    print(round(os.path.getsize(os.path.join(download_folder, file_name)) / (1024 ** 2)), 'MB')

finally:
    driver.quit()
