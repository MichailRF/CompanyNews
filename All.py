from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By
import time
import pymysql
from config import host, user, password, db_name

options = chrome_options()
driver = webdriver.Chrome(executable_path="C:\\Users\\mihsa\\PycharmProjects\\"
                                          "pythonProject\\chromedriver\\chromedriver.exe", options=options)


def go_url():
    url = "https://ru.investing.com/equities/russia"
    driver.get(url)
    cookie = {"name": "new_user_guidance", "value": "true", "domain": ".investing.com"}
    driver.add_cookie(cookie)
    driver.get(url)
    time.sleep(2)


go_url()
print("готово")
item_list = driver.find_elements(By.TAG_NAME, "td")
print("item_list = ", len(item_list))
# index = 0
# for i in item_list:
#     print(i.text, index)
#     index += 1
index = 0
while index < 328:
    f1 = item_list[index].text
    item_list[index].click()
    data = driver.find_elements(By.TAG_NAME, "time")
    data_1 = data[1].text
    data_2 = data[2].text
    data_3 = data[3].text
    (driver.find_elements(By.CLASS_NAME,
                          'inv-link' and 'text-secondary' and 'font-bold' and 'text-sm' and 'whitespace-normal'))[
        0].click()
    if driver.find_elements(By.CLASS_NAME, 'bp3-portal'):
        news = driver.find_elements(By.CLASS_NAME, 'text-base')
    else:
        news = driver.find_elements(By.CLASS_NAME, 'WYSIWYG' and 'articlePage')
    text_1 = ''
    for i in range(0, len(news)):
        text_1 += news[i].text
    go_url()
    item_list = driver.find_elements(By.TAG_NAME, "td")
    item_list[index].click()
    (driver.find_elements(By.CLASS_NAME,
                          'inv-link' and 'text-secondary' and 'font-bold' and 'text-sm' and 'whitespace-normal'))[
        1].click()
    if driver.find_elements(By.CLASS_NAME, 'bp3-portal'):
        news = driver.find_elements(By.CLASS_NAME, 'text-base')
    else:
        news = driver.find_elements(By.CLASS_NAME, 'WYSIWYG' and 'articlePage')
    text_2 = ''
    for i in range(0, len(news)):
        text_2 += news[i].text
    go_url()
    item_list = driver.find_elements(By.TAG_NAME, "td")
    item_list[index].click()
    (driver.find_elements(By.CLASS_NAME,
                          'inv-link' and 'text-secondary' and 'font-bold' and 'text-sm' and 'whitespace-normal'))[
        2].click()
    if driver.find_elements(By.CLASS_NAME, 'bp3-portal'):
        news = driver.find_elements(By.CLASS_NAME, 'text-base')
    else:
        news = driver.find_elements(By.CLASS_NAME, 'WYSIWYG' and 'articlePage')
    text_3 = ''
    for i in range(0, len(news)):
        text_3 += news[i].text
    text = data_1, text_1, data_2, text_2, data_3, text_3
    print(text)
    go_url()
    index = index + 1
    item_list = driver.find_elements(By.TAG_NAME, "td")
    f2 = item_list[index].text
    index = index + 1
    f3 = item_list[index].text
    index = index + 1
    f4 = item_list[index].text
    index = index + 1
    f5 = item_list[index].text
    index = index + 1
    f6 = item_list[index].text
    index = index + 1
    f7 = item_list[index].text
    index = index + 1
    f8 = item_list[index].text
    index = index + 1
    print(f1, f2, f3, f4, f5, f6, f7, f8)
    ptr = (f'{f1}', f'{f2}', f'{f3}', f'{f4}', f'{f5}', f'{f6}', f'{f7}', f'{f8}', f'{text}')
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO `msd` (name, price, max, min, chage, change_procent, volume, time, news) VALUES {ptr};"
                cursor.execute(insert_query)
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)

driver.quit()
