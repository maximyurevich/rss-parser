"""RSS parser"""
import logging
import asyncio
import feedparser
from dateutil import parser


logging.basicConfig(level=logging.INFO)


async def get_rss_items(url: str) -> list[dict[str, str]]:
    """get rss items

    Args:
        url (str): rss link

    Returns:
        list[dict[str, str]]
            List of news entries
    """

    feed = feedparser.parse(url)

    data: list[dict[str, str]] = []

    for entry in feed["entries"]:
        entry_dict = {
            "title": entry["title"],
            "category": entry["category"],
            "link": entry["link"],
            "published": [
                parser.parse(entry["published"]).day,
                parser.parse(entry["published"]).time().hour,
                parser.parse(entry["published"]).time().minute,
            ],
        }

        data.append(entry_dict)

    data.reverse()

    return data

if __name__ == "__main__":
    asyncio.run(get_rss_items("https://zelwa.by/feed/"))