from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
ops = ChromeOptions()
ops.add_argument("--disable notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)