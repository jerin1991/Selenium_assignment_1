from assignment1 import open_browser as ob
# from assignment1 import open_amazon as oa
ob.driver.get("https://www.flipkart.com/")
ob.driver.find_element_by_class_name('_2KpZ6l _2doB4z').click()