import os
from datetime import datetime
import time

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
    driver.get(url="https://sermessenger.energytransfer.com/ipost/SER/capacity/operationally-available-by-location?max=10")

    wait = WebDriverWait(driver, 10)

    date_elem = wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='gasDay']")
        )
    )
    date_elem.clear()
    date_elem.send_keys(now.strftime('%m/%d/%Y'))

    driver.find_element_by_xpath("/html/body/div/div/article/section/form/button").click()
    time.sleep(3)

    cycle_elem = wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='cycleDesc']")
        )
    )
    cycle = cycle_elem.get_attribute('value')

    post_datetime_elem = driver.find_element_by_xpath("//*[@id='wrapper-main']/div/article/section/p[2]")
    post_datetime = post_datetime_elem.text

    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver.get_screenshot_as_file(f'{dir_path}/../074_screens/screen:{now}.png')

    print(f"{now},{cycle},{post_datetime}")
except Exception as e:
    print(f"{now},{str(e)},0")
finally:
    driver.close()
