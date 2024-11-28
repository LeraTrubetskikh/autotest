# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
try:
    # Авторизоваться на сайте https://fix-online.sbis.ru/
    driver.get('https://fix-online.sbis.ru/')
    sleep(2)
    login = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]')[0].find_element(By.TAG_NAME, 'input')
    login.send_keys('Lera', Keys.ENTER)
    sleep(2)

    password = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]')[1].find_element(By.TAG_NAME, 'input')
    password.send_keys('qwerty123', Keys.ENTER)
    sleep(5)

    # Перейти в реестр Контакты
    # contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]').find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    # contacts.click()
    driver.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(3)

    # Отправить сообщение самому себе
    button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    button.click()
    sleep(5)
    search = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]').find_element(By.TAG_NAME, 'input')
    search.send_keys('Трубецких', Keys.ENTER)
    sleep(2)
    user = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"]')
    user.click()
    sleep(3)
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message.click()
    message.send_keys('тут что-то написано')
    sleep(3)
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    message.click()
    sleep(5)

    # Убедиться, что сообщение появилось в реестре
    check_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"]') #.find_element(By.TAG_NAME, 'p')
    # assert check_message.text == 'тут что-то написано'

    # Удалить это сообщение и убедиться, что удалили
    action = ActionChains(driver)
    action.move_to_element(check_message)
    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    action.move_to_element(delete_button)
    action.context_click()
    action.perform()
    sleep(2)

    # Для сдачи задания пришлите код и запись с экрана прохождения теста
finally:
    driver.quit()
