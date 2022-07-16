from selenium import webdriver
import time

url = "https://test.mensa.no/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(3)
xpath_button_18_50 = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
# button_18_50 = driver.find_element_by_xpath(xpath_button_18_50) устарел
button_18_50 = driver.find_element('xpath', xpath_button_18_50)
button_18_50.click()
time.sleep(3)
xpath_start_button = '/html/body/div[2]/main/cach/div[2]/div/div/div/div[2]/button'
button_start_button = driver.find_element('xpath', xpath_start_button)
button_start_button.click()
time.sleep(3)
# xpath_answer_1_a = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
# button_answer_1_a = driver.find_element('xpath',xpath_answer_1_a)
# button_answer_1_a.click()
# time.sleep(3)
# xpath_answer_2_a = '/html/body/div[2]/main/cach/div[3]/div[2]/div[3]/div[1]/div/img'
# button_answer_2_a = driver.find_element('xpath',xpath_answer_2_a)
# button_answer_2_a.click()
# time.sleep(3)
# xpath_answer_3_b = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[2]/div/img'
# button_answer_3_b = driver.find_element('xpath',xpath_answer_3_b)
# button_answer_3_b.click()
# time.sleep(3)
# for i in range(1,35+1):
#     xpath_answer_a = f'/html/body/div[2]/main/cach/div[3]/div[{i}]/div[3]/div[1]/div/img'
#     button_answer_a = driver.find_element('xpath',xpath_answer_a)
#     button_answer_a.click()
#     time.sleep(1)
#
# xpath_finish_button = '/html/body/div[2]/main/cach/div[3]/div[35]/div[5]/div/button[3]'
# button_finish_button = driver.find_element('xpath',xpath_finish_button)
# button_finish_button.click()
# time.sleep(3)
# xpath_finish_window_button = '/html/body/div[2]/main/cach/div[3]/div[35]/div[5]/div/button[3]'
# button_finish_window_button = driver.find_element('xpath',xpath_finish_window_button)
# button_finish_window_button.click()
# time.sleep(3)

# user1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 1}#'a' - 1, 'b' - 2 #номер вопроса: номер ответа
# for key in user1:
#     #key - номер вопроса  user1[key] - номера ответа
#     xpath_answer_a = f'/html/body/div[2]/main/cach/div[3]/div[{key}]/div[3]/div[{user1[key]}]/div/img'
#     button_answer_a = driver.find_element('xpath',xpath_answer_a)
#     button_answer_a.click()
#     time.sleep(1)
import random

for key in range(1, 35 + 1):
    # key - номер вопроса  user1[key] - номера ответа
    xpath_answer_a = f'/html/body/div[2]/main/cach/div[3]/div[{key}]/div[3]/div[{random.randint(1, 6)}]/div/img'
    button_answer_a = driver.find_element('xpath', xpath_answer_a)
    button_answer_a.click()
    time.sleep(1)

xpath_finish_button = '/html/body/div[2]/main/cach/div[3]/div[35]/div[5]/div/button[3]'
button_finish_button = driver.find_element('xpath', xpath_finish_button)
button_finish_button.click()
time.sleep(3)
xpath_finish_window_button = '/html/body/div[2]/main/cach/div[6]/div/div/div[3]/button[2]'
button_finish_window_button = driver.find_element('xpath', xpath_finish_window_button)
button_finish_window_button.click()
time.sleep(3)
