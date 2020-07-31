from Login import Login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

urlInstagram = "https://www.instagram.com/"
urlYandex = "https://yandex.ru/"


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


user = User('facts_motiv', 'Zoro987')

# def login_and_subscribe():
#     login_handler = Login(driver, By)
#     login_handler.login(urlInstagram, user.name, user.password)
#     login_handler.subscribe()
#     print('Вышли...')

def login_and_un_subscribe():
    login_handler = Login(driver, By)
    login_handler.login(urlInstagram, user.name, user.password)
    driver.get(urlInstagram + user.name)
    subscribe_link = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
    subscribe_link.click()
    links = driver.find_elements(By.XPATH, '//button[text()="Подписки"]')
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(2)

    count = 0

    try:
        for link in links:
            link.click()
            time.sleep(1)
            cancel_btn = driver.find_element(
                By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[1]')
            cancel_btn.click()
            print('Отписка закончилась...')
    except:
        print("Something went wrong")
    finally:
        time.sleep(10)
        driver.quit()


if __name__ == '__main__':
    login_and_un_subscribe()
