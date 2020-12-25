import asyncio
import aiohttp
import time
import requests


async def download_all_sites(site_urls):
	async with aiohttp.ClientSession() as session:
		tasks = []
		for site_url in site_urls:
			task = asyncio.ensure_future(download_site(session, site_url))
			tasks.append(task)
		await asyncio.gather(*task, return_exceptions=True)


def download_site(session, site_url):
	print(site_url)
	with session.get(site_url) as response:
		print("Read {0} from {1}".format(response.content_length, url))


if __name__ == '__main__':
	start = time.time()

	site_urls = [
	    "https://www.jython.org",
        "http://olympus.realpython.org/dice",
	] * 1

	asyncio.get_event_loop().run_until_complete(download_all_sites(site_urls))

	end = time.time()
	print(f"Downloaded {len(sites)} sites in {end - start} seconds")