import asyncio
import aiohttp

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

headers = {
    "X-CMC_PRO_API_KEY": "your api coinmarketcap"
}

params = {
    "symbol": "BTC,ETH,SOL,NEAR,THETA,LTC",
    "convert": "USDT"
}

async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            getting_data = await response.json()
            
            for name, information in getting_data["data"].items():
                name = information["name"]
                symbol = information["symbol"]
                price = information["quote"]["USDT"]["price"]
                change_24h = information["quote"]["USDT"]["percent_change_24h"]
                change_7d = information["quote"]["USDT"]["percent_change_7d"]
                volume_24h = information["quote"]["USDT"]["volume_24h"]
    
                print(f"{name} | {symbol} | {price:.2f} USDT | Change for 24h : {change_24h:.2f}% | Change for 7d : {change_7d:.2f}% | Volume for 24h : {volume_24h:.2f} USDT")

            
asyncio.run(get_data())
