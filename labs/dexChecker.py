import asyncio
import aiohttp
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

"""You can add your own Subgraphs 
    if needed to compare prices on dex and choose 
    the most optimal one for you!"""
    

uniswap = "https://gateway.thegraph.com/api/your API Thegraph/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"
sushiswap = "https://gateway.thegraph.com/api/your API Thegraph/subgraphs/id/5nnoU1nUFeWqtXgbpC54L9PWdpgo7Y9HYinR3uTMsfzs"
pancakeswap = "https://gateway.thegraph.com/api/your API Thegraph/subgraphs/id/CJYGNhb7RvnhfBDjqpRnD3oxgyhibzc7fkAMa38YV3oS"

query = """
{
    factories(first: 5) {
    id
    poolCount
    txCount
    totalVolumeUSD
  }
  bundles(first: 5) {
    id
    ethPriceUSD
    }
}
"""

async def uni(): 
    async with aiohttp.ClientSession() as session:
        async with session.post(uniswap, json={"query": query}) as rqst:
            data = await rqst.json()
            
            for bundle in data["data"]["bundles"]:
                ethPriceUSD = float(bundle["ethPriceUSD"])
                logging.info(f"Price ETH for Uniswap: {ethPriceUSD:.2f}")
                
async def sushi():
    async with aiohttp.ClientSession() as session:
        async with session.post(sushiswap, json={"query": query}) as rqst:
            data = await rqst.json()
            
            for bundle in data["data"]["bundles"]:
                ethPriceUSD = float(bundle["ethPriceUSD"])
                logging.info(f"Price ETH for SushiSwap: {ethPriceUSD:.2f}")
                
async def pancake():
    async with aiohttp.ClientSession() as session:
        async with session.post(pancakeswap, json={"query": query}) as rqst:
            data = await rqst.json()
            
            for bundle in data["data"]["bundles"]:
                ethPriceUSD = float(bundle["ethPriceUSD"])
                logging.info(f"Price ETH for PancakeSwap: {ethPriceUSD:.2f}")
                
asyncio.run(uni())
asyncio.run(sushi())
asyncio.run(pancake())
