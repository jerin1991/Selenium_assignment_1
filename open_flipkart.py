import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from assignment1 import open_browser as ob
# from assignment1 import open_amazon as oa
ob.driver.get("https://www.flipkart.com/")
ob.driver.maximize_window() #maximise window
ob.driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click() #close notification
time.sleep(5)
ob.driver.find_element_by_xpath("//input[@name='q']").send_keys("iPhone XR (64GB) - Yellow", Keys.ENTER) #search for iPhone XR (64GB) - Yellow and press enter
time.sleep(5)
ob.driver.find_element_by_xpath("(//div[@class='_4rR01T'])[2]").click() #search for particular phone in list
time.sleep(5)

print("parent window title:",ob.driver.title) # parent window title
print("parent window id:",ob.driver.current_window_handle) #parent window id

wins = ob.driver.window_handles
for x in wins:
    ob.driver.switch_to_window(x)

print("child window title:",ob.driver.title) #child window title
print("child window id:",ob.driver.current_window_handle) #child window id

def flipkart_price():
    price = ob.driver.find_element_by_xpath("//div[@class='_30jeq3 _16Jk6d']").text #get price by xpath and converting to text
    print("price of phone:", price) # printing price


flipkart_price() #calling function to ren in this class
ob.driver.quit() #quit browser