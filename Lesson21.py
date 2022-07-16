from selenium import webdriver
import time

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.selenium.dev/")
# driver.get_screenshot_as_file('site1.png')
# time.sleep(5)
# driver.get("https://solar-online.com.ua/ru/avtonomnye-zaryadnye-stancii-na-solnechnyh-batareyah/mobilnye/")
# driver.get_screenshot_as_file('site2.png')

# sites = ["https://store.steampowered.com/","https://www.tinkercad.com/","https://www.w3schools.com/html/"]
# driver = webdriver.Chrome()
# time.sleep(5)
# #driver.set_window_position(1700,300)
# driver.maximize_window()
# count = 0
# for site in sites:
#     driver.get(site)
#     time.sleep(5)
#     driver.get_screenshot_as_file(f'site{count}.png')
#     count = count + 1
#


driver = webdriver.Chrome()
time.sleep(5)
# driver.set_window_position(1700,300)
driver.maximize_window()
count = 0
for i in range(2, 100):
    url = f"https://ebanoe.it/page/{i}/"
    driver.get(url)
    time.sleep(7)
    driver.get_screenshot_as_file(f'site{count}.png')
    count = count + 1
