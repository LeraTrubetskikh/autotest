# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import uuid
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
    sleep(1)

    password = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]')[1].find_element(By.TAG_NAME, 'input')
    password.send_keys('qwerty123', Keys.ENTER)
    sleep(5)

    # Перейти в реестр Контакты
    driver.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(3)

    # Отправить сообщение самому себе
    # Нажать кнопку добавить диалог
    button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    button.click()
    sleep(5)
    # В строку поиска ввести фамилию
    search = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]').find_element(By.TAG_NAME, 'input')
    search.send_keys('Трубецких', Keys.ENTER)
    sleep(2)
    # Открыть первого в списке
    user = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"]')
    user.click()
    sleep(3)
    # Ввести текст сообщения
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message.click()
    sleep(1)
    message_text = str(uuid.uuid4())
    message.send_keys(message_text)
    sleep(3)
    # Отправить сообщение
    message_send = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    message_send.click()
    sleep(5)

    # Убедиться, что сообщение появилось в реестре
    check_message = (driver.find_elements(By.CSS_SELECTOR, '.msg-entity-expander.ws-flexbox.ws-flex-column.msg-entity-expander_collapsed.controls-fontsize-m')[0]
                     .find_element(By.TAG_NAME, 'p'))
    assert check_message.text == message_text

    # Удалить это сообщение и убедиться, что удалили
    check_message.click()
    sleep(2)
    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="remove"]')
    delete_button.click()
    sleep(2)
    check_message = (driver.find_elements(By.CSS_SELECTOR,
                                          '.msg-entity-expander.ws-flexbox.ws-flex-column.msg-entity-expander_collapsed.controls-fontsize-m')[0]
                     .find_element(By.TAG_NAME, 'p'))
    assert check_message.text != message_text

finally:
    driver.quit()
