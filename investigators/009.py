import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

now = datetime.now()

try:
    driver.get(url="https://peplmessenger.energytransfer.com/ipost/PEPL/capacity/operationally-available-by-location")

    cycle_elem = driver.find_element_by_xpath("//*[@id='cycleDesc']")
    cycle = cycle_elem.get_attribute('value')

    post_datetime_elem = driver.find_element_by_xpath("//*[@id='wrapper-main']/div/article/section/p[2]")
    post_datetime = post_datetime_elem.text

    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver.get_screenshot_as_file(f'{dir_path}/../009_screens/screen:{now}.png')

    print(f"{now},{cycle},{post_datetime}")
except Exception as e:
    print(f"{now},{str(e)},0")
finally:
    driver.close()
