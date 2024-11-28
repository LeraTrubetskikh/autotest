# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    # Перейти на https://sbis.ru/
    driver.get('https://sbis.ru/')
    assert driver.current_url == 'https://sbis.ru/'
    sleep(2)

    # Перейти в раздел "Контакты"
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu.js-ContactsMenu')
    assert contacts.text == 'Контакты'
    contacts.click()
    sleep(1)
    link = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu.js-ContactsMenu').find_element(By.CSS_SELECTOR,'.sbisru-link.sbis_ru-link')
    assert link.get_attribute('href') == 'https://sbis.ru/contacts'
    link.click()
    sleep(1)

    # Найти баннер Тензор, кликнуть по нему
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__border-left.sbisru-Contacts__border-left--border-xm').find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    assert banner.get_attribute('title') == 'tensor.ru'
    banner.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)

    # Перейти на https://tensor.ru/
    driver.get('https://tensor.ru/')
    assert driver.current_url == 'https://tensor.ru/'

    # Проверить, что есть блок новости "Сила в людях"
    news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    news_title = news.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-title.tensor_ru-pb-16')
    assert news_title.text == 'Сила в людях'
    sleep(2)

    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    link = news.find_element(By.CSS_SELECTOR, '.tensor_ru-link.tensor_ru-Index__link')
    assert link.get_attribute('href') == 'https://tensor.ru/about'
    link.click()
    sleep(2)

finally:
    driver.quit()
