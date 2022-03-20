import time

from assignment1 import open_amazon
time.sleep(5)
from assignment1 import open_flipkart
time.sleep(5)
price_az = open_amazon.amazon_price()
price_fk = open_flipkart.flipkart_price()
