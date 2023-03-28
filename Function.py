from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
import os
import pymysql
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
options = chrome_options()
s = Service((os.getenv('executable_path')))
driver = webdriver.Chrome(service=s, options=options)


def go_url():
    url = (os.getenv('url'))
    driver.get(url)


def class_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.CLASS_NAME, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.CLASS_NAME, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.CLASS_NAME, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.CLASS_NAME, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


def tag_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.TAG_NAME, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.TAG_NAME, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.TAG_NAME, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.TAG_NAME, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


def name_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.NAME, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.NAME, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.NAME, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.NAME, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


def id_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.ID, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.ID, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.ID, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.ID, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


def xpath_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.XPATH, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.XPATH, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.XPATH, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.XPATH, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


def css_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.CSS_SELECTOR, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.CSS_SELECTOR, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.CSS_SELECTOR, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.CSS_SELECTOR, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


def text_interpreter(element, index=99999, clickable=00):
    if index == 99999:
        if clickable == 00:
            return driver.find_elements(By.LINK_TEXT, element)
        elif clickable != 00:
            index_element = driver.find_elements(By.LINK_TEXT, element)
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()
    elif index != 99999:
        if clickable == 00:
            return driver.find_elements(By.LINK_TEXT, element)[index]
        elif clickable != 00:
            index_element = driver.find_elements(By.LINK_TEXT, element)[index]
            return WebDriverWait(driver, 20).until(EC.element_to_be_clickable(index_element)).click()


control_dict = {
    'class': class_interpreter,
    'tag': tag_interpreter,
    'name': name_interpreter,
    'id': id_interpreter,
    'xpath': xpath_interpreter,
    'css': css_interpreter,
    'text': text_interpreter
}

# control_dict[type](arguments)


def import_sql(name_table, information):
    try:
        connection = pymysql.connect(
            host=os.getenv('host'),
            port=3306,
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database'),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO {name_table} (name, price, max, min, chage, change_procent, volume, time, news) VALUES {information};"
                cursor.execute(insert_query)
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)
