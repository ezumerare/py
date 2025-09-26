from bs4 import BeautifulSoup
import asyncio
import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

cmc = "https://coinmarketcap.com"
cmc_connect = requests.get(cmc)
logging.info(f"cmc - {cmc_connect.status_code}")

params = {}

class CoinMarketCap():
    def __init__(self, name="", symbol="", price=""):
        self.name = name
        self.symbol = symbol
        self.price = price

    async def pars_cmc(self, html):
        cmc_view = BeautifulSoup(html, "html.parser")
        names = cmc_view.find_all("p", class_="sc-65e7f566-0 iPbTJf coin-item-name")
        symbols = cmc_view.find_all("p", class_="sc-65e7f566-0 byYAWx coin-item-symbol")
        prices = cmc_view.find_all("div", class_="sc-fa25c04c-0 eAphWs")
        for name_info, symbol_info, price_info in zip(names[:10], symbols[:10], prices[:10]):
            name = name_info.get_text()
            symbol = symbol_info.get_text()
            price = price_info.get_text()
            
            logging.info(f"{name} ({symbol}) | Price - {price}")
        
html = cmc_connect.text
obj = CoinMarketCap()
asyncio.run(obj.pars_cmc(html))
