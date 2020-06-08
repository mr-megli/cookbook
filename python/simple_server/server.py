import aiohttp
from aiohttp import web

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


# Routes definition which is then used for setting up the actual paths the
# handlers are listening at.
routes = web.RouteTableDef()


@routes.get('/search')
async def query_titles(request: web.Request):
    """Returns published titles.

    Args:
        request (web.Request): [description]
    """
    search_term = request.query['q']
    resp = await search(search_term)

    title_list = [{'title': item['title'], 'date': item['start_year']}
                  for item in resp['items']]
    return web.json_response(title_list)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
