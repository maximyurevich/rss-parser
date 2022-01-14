import asyncio
import asyncio
from rss_parser import get_rss_items
import logging


logging.basicConfig(level=logging.INFO)


async def main(url: str):
    logging.info(await get_rss_items(url))
    return await get_rss_items(url)

if __name__ == "__main__":
    asyncio.run(main("https://zelwa.by/feed/"))