import time

from selenium.webdriver.common.keys import Keys

from assignment1 import open_browser as ob #import browser from open_browser class
ob.driver.get("https://www.amazon.in/") #calling amazon.in
ob.driver.maximize_window() #maximising window
ob.driver.find_element_by_id("twotabsearchtextbox").send_keys("iPhone 11 (64GB) - Yellow", Keys.ENTER) #finding element of search bar and searching for iphone
time.sleep(5)
ob.driver.find_element_by_xpath("//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']/span[contains(text(), 'iPhone 11 (64GB) - Yellow')]").click() #click on first item from list after searching in amazon
time.sleep(10)
print("parent page id:", ob.driver.current_window_handle)
print("parent page title", ob.driver.title)

wins = ob.driver.window_handles
for x in wins:
    ob.driver.switch_to_window(x)

print("child page id:", ob.driver.current_window_handle)
print("child page title", ob.driver.title)

def amazon_price():
    price = ob.driver.find_element_by_xpath("//span[@class='a-price a-text-price a-size-medium apexPriceToPay']").text
    print("price in amazon:", price)

amazon_price()
# price = ob.driver.find_element_by_xpath("(//span[@class='a-price-whole'])[1]")
# print(price.text)
#
# # ob.driver.find_element_by_xpath("(//span[@class='a-size-medium a-color-base a-text-normal'])[1]").click()
# # time.sleep(10)
#
# # ob.driver.get("https://www.amazon.in/New-Apple-iPhone-11-64GB/dp/B08L8CV8GH/ref=sr_1_1?crid=1RO1NDTNU2BLL&keywords=iPhone+XR+%2864GB%29+-+Yellow&qid=1647259660&sprefix=iphone+xr+64gb+-+yellow%2Caps%2C631&sr=8-1")
# # price = ob.driver.find_element_by_xpath("//span[@class='a-price a-text-price a-size-medium apexPriceToPay']")
# # print(price.get_attribute('href'))
ob.driver.quit()
