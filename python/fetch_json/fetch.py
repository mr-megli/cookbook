"""Fetches content from a specific server using HTTP.
"""

import asyncio
import aiohttp

SERVER_URL = "https://chroniclingamerica.loc.gov/search/titles/results/?terms={search_term}&format=json"


async def search(search_term: str):
    """Searches historic newspaper articles from the library of congress.

    Args:
        search_term (str): Search term to search for.
    """
    async with aiohttp.ClientSession() as session:
        response: aiohttp.ClientResponse
        async with session.get(SERVER_URL.format(search_term=search_term)) as response:
            return await response.json()


async def main():
    resp = await search('switzerland')
    titles = [item['title'] for item in resp['items']]
    print(titles)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
