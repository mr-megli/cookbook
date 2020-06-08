This example shows how to make *async* HTTP requests using

* `asyncio`
* `aiohttp` ([doc](https://pypi.org/project/aiohttp/))

In order to run it, `aiohttp` needs to be installed first, which can be done
with

```bash
$ pip install aiohttp
```

The example fetches news-articles from `https://chroniclingamerica.loc.gov/`.