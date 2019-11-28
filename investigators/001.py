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
    driver.get(url="https://services.kernrivergas.com/portal/Informational-Postings/Capacity/Operationally-Available")

    retrieve_button = driver.find_element_by_xpath("//*[@id='dnn_ctr436_OperAvailable_btnTest']")
    retrieve_button.click()

    wait = WebDriverWait(driver, 10)
    cycle_elem = wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='dnn_ctr436_OperAvailable_DataGrid1']/tbody/tr[2]/td[4]")
        )
    )

    post_date = driver.find_element_by_xpath("//*[@id='dnn_ctr436_OperAvailable_TSP1_DataGrid1']/tbody/tr[2]/td[3]")
    post_time = driver.find_element_by_xpath("//*[@id='dnn_ctr436_OperAvailable_TSP1_DataGrid1']/tbody/tr[2]/td[4]")

    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver.get_screenshot_as_file(f'{dir_path}/../001_screens/screen:{now}.png')

    print(f"{now},{cycle_elem.text},{post_date.text} {post_time.text}")
except Exception as e:
    print(f"{now},{str(e)},0")
finally:
    driver.close()
