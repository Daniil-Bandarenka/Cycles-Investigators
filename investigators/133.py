from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()

try:
    driver.get(url="https://transmission.wbienergy.com/informational_postings/capacity/operational_capacity_locations.aspx")

    retrieve_button = driver.find_element_by_xpath("//*[@id='btnRetrieve']")
    retrieve_button.click()

    wait = WebDriverWait(driver, 10)
    cycle_elem = wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, "//*[@id='lblCycle']")
        )
    )

    print(f"{datetime.now()} : {cycle_elem.text}")
except Exception as e:
    print(f"{datetime.now()} : {str(e)}")
finally:
    driver.close()
