"""Main file"""
import logging
import asyncio
from rss_parser import collect_rss_items


logging.basicConfig(level=logging.INFO)


async def main(url: str):
    """Main function"""
    logging.info(await collect_rss_items(url))
    return await collect_rss_items(url)

if __name__ == "__main__":
    asyncio.run(main("https://www.vesti.ru/vesti.rss"))