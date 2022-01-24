"""RSS parser for news sites with categories"""
import logging
import asyncio
import feedparser


logging.basicConfig(level=logging.INFO)


async def get_rss_items(url: str):
    """get rss items

    Args:
        url (str): rss link

    Returns:
        list[dict[str, str]]
            List of news entries
    """

    feed = feedparser.parse(url)

    for entry in feed["entries"]:
        yield {
            "title": entry["title"],
            "category": entry["category"],
            "link": entry["link"],
            "published": entry["published"]
        }

async def collect_rss_items(url: str):
    """collect rss items

    Args:
        url (str): rss link

    Returns:
        list[dict[str, str]]
            List of news entries
    """
    return [item async for item in get_rss_items(url)]

if __name__ == "__main__":
    asyncio.run(collect_rss_items("https://www.vesti.ru/vesti.rss"))
