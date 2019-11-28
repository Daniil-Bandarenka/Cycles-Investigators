import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

now = datetime.now()

try:
    driver.get(url="https://peplmessenger.energytransfer.com/ipost/PEPL/capacity/operationally-available-by-location")

    wait = WebDriverWait(driver, 10)
    cycle_elem = wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='cycleDesc']")
        )
    )
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
