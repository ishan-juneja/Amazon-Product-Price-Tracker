# Amazon-Product-Price-Tracker
This program tracks an amazon product and informs whether you should purchase it or not based on its historical pricing.

## Structure
- `PriceTracker.py` retrieves the current and average historical pricing of the product
- `NotificationClass.py` informs the user via email of the product details 
- `main.py` ties together all classes and behaves as the nucleus
## Dependencies & Configurations
1. The [Beautiful Soup Library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to webscrape the current price off of amazon and the average historical price off of [camelcamelcamel](https://camelcamelcamel.com/).
2. The [Tequila Kiwi API](https://tequila.kiwi.com/) to find all our flight info.
   - Retrieve your **API_KEY** & **AFFIL_ID** once you create your account
   - Add to `flight_search.py`
3. The [Twilio API](https://www.twilio.com/docs) to message ourselves our details of the flight.
   - Retrieve your **ACCOUNT_SID** & **AUTH_TOKEN** once you create your account
   - Add to `notification_class.py`
   - Change the phone numbers to your Twilio Assigned Number and your personal phone number within the `notification_class.py` in the `notify` method

## Demo
