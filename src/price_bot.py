import requests
from bs4 import BeautifulSoup

class PriceBot(object):
    URL = 'https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/p2083183'

    def get_price(self):
        r = requests.get(self.URL)
        content = r.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find("span", {"itemprop": "price", "class": "now-price"})
        string_price = element.text.strip() # £129.00
        price_without_symbol = string_price[1:]
        price = float(price_without_symbol)
        return price
# if price < 200:
#     print('You should buy the chair!')
#     print('The current price is {}'.format(price))
# else:
#     print('Do not buy, it\'s too expensive!')