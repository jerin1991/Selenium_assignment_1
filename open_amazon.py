import time

from selenium.webdriver.common.keys import Keys

from assignment1 import open_browser as ob
ob.driver.get("https://www.amazon.in/")
ob.driver.maximize_window()
ob.driver.find_element_by_id("twotabsearchtextbox").send_keys("iPhone XR (64GB) - Yellow")
time.sleep(5)
ob.driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(10)
try:
    ob.driver.find_elements_by_class_name("a-size-medium a-color-base a-text-normal").click()
    time.sleep(10)
except:
    print("element not found")
ob.driver.quit()
