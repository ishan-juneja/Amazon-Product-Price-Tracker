import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class PriceTracking:
    def __init__(self, product_url):
        self.product_url = product_url
        self.soup = self.getSoup()


    def getSoup(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        ua = UserAgent()
        hdr = {'User-Agent': ua.random,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        web_info = requests.get(self.product_url,
                                headers=hdr)
        return BeautifulSoup(web_info.text, 'html.parser')

    def findCurrentPrice(self):
        # to get the actual link we want we need our device https header and to bypass the Captcha
        return self.soup.find(name="span", class_="a-price-whole").text + self.soup.find(name="span", class_="a-price-fraction").text

    def findProductName(self):
        return self.soup.find(name="span", id="productTitle").text

    def findAverageProductPrice(self, product_id):
        web_info = requests.get(f"https://camelcamelcamel.com/product/{product_id}",
                                headers={
                                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                                    "Accept-Language": "en-US,en;q=0.9"})

        soup = BeautifulSoup(web_info.text, 'html.parser')
        info = soup.find(name="tbody")
        if(info == "none"):
            return "none"
        else:
            temp_list = []
            for i in info:
                temp_list.append(i.text.strip())

            average_price = ""
            for char in temp_list[7]:
                if char.isnumeric() or char == '.':
                    average_price += char
            return float(average_price)

    def findProductID(self):
        link = self.soup.find(name="link", rel="canonical").get("href")
        link = link[len(link)-10: len(link)]
        return link