# Amazon-Product-Price-Tracker
This program tracks an Amazon product and informs whether you should purchase it or not based on its historical pricing.

## Structure
- `PriceTracker.py` retrieves the current and average historical pricing of the product
- `NotificationClass.py` informs the user via email of the product details 
- `main.py` ties together all classes and behaves as the nucleus
## Dependencies & Configurations
1. The [Beautiful Soup Library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to web scrape the current price off of Amazon and the average historical price off of [camelcamelcamel](https://camelcamelcamel.com/).
2. The [Fake User Agent Library](https://pypi.org/project/fake-useragent/) to bypass the Captcha bot checks during web scraping
3. The [SMPTLIB Library](https://docs.python.org/3/library/smtplib.html) to send the product details email
   - `NotificationClass.py` will require an **Email** & **Email Password** to send the email from and an **Email** to send the email to!


## Demo
This is the product we will be tracking!
![Screenshot 2023-07-05 at 10 55 58 PM](https://github.com/ishan-juneja/Amazon-Product-Price-Tracker/assets/69048541/7f60ca24-e982-4cc8-9d57-f008acbd1e10)


After entering the link into my console, the program informed me whether or not to buy the product based on its comparison with the average historical price!
<img width="1412" alt="Screenshot 2023-07-05 at 10 55 16 PM" src="https://github.com/ishan-juneja/Amazon-Product-Price-Tracker/assets/69048541/424882dc-f444-41c9-b754-912960e6f0d8">
