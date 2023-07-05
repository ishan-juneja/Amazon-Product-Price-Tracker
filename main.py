import requests
from bs4 import BeautifulSoup

import NotificationClass
import PriceTracker

url_product = input("Which Amazon Product are you attempting to track? (enter the product url): ")
PT = PriceTracker.PriceTracking(url_product)
price = float(PT.findCurrentPrice())
product_name = PT.findProductName().strip()
product_id = PT.findProductID()


notifier = NotificationClass.Notifier()
watch_price = round(PT.findAverageProductPrice(PT.findProductID()) * 0.95,2)
if(PT.findAverageProductPrice(PT.findProductID()) == "none"):
    watch_price = float(input("Our servers were unable to locate the average price of the product concurrently. Please enter at which price"
          " you want to purchase your product! Enter as: ( __.__ , eg. 9.70)"))

if(price < watch_price):
    print("YAY!")
    print(f"Current product price is {price} while the watch price is {watch_price}")
    notifier.notify(product_price=price,product_link=url_product,product_name=product_name)
else:
    print(f"Current product price is {price} while the lowered watch price is {watch_price}")


