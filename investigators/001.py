from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()

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

    print(f"{datetime.now()} : {cycle_elem.text}")
except Exception as e:
    print(f"{datetime.now()} : {str(e)}")
finally:
    driver.close()
