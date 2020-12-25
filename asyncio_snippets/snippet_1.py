import asyncio
import time
import aiohttp
import requests


# --------------------------------------------------------------------------------
# async fucntion - coroutine - measure
async def measure(html:str) -> int:
	return len(html)

# async function - coroutine - fetch
async def fetch(url:str):
	async with aiohttp.ClientSession() as session:
		response = await session.get(url)
		html = await response.text()
		length = await measure(html)
		return length

# async function - coroutine - main
async def main(urls:list) -> list:
	result = await asyncio.gather(*[fetch(url) for url in urls])
	return result

# async function - coroutine - non_concur_main
async def non_concur_main(urls:list) -> list:
	result = []
	result.append(await fetch(urls[0]))
	result.append(await fetch(urls[1]))
	result.append(await fetch(urls[2]))
	return result

# --------------------------------------------------------------------------------
def sync_measure(html:str) -> int:
	return len(html)

def sync_fetch(url:str):
	html = requests.get(url).text
	return sync_measure(html)

def sync_main(urls:list):
	result = [sync_fetch(url) for url in urls]
	return result

# --------------------------------------------------------------------------------
if __name__ == '__main__':
	urls = [
		'https://dev.to/v_it_aly/asyncio-basic-fundamentals-4i5m',
		'https://dev.to/v_it_aly/asyncio-basic-fundamentals-4i5m',
		'https://dev.to/v_it_aly/asyncio-basic-fundamentals-4i5m'
	]

	# Asynchronous - running coroutines concurrently - gather
	start = time.time()
	result = asyncio.run(main(urls))
	print(result)
	end = time.time()
	print(f"Downloaded {len(urls)} sites in {end - start} seconds.\n")

	# Asynchronous - running coroutines non-concurrently
	start = time.time()
	result = asyncio.run(non_concur_main(urls))
	print(result)
	end = time.time()
	print(f"Downloaded {len(urls)} sites in {end - start} seconds.\n")

	# Synchronous - running asynchronously with for loop
	start = time.time()
	result = sync_main(urls)
	print(result)
	end = time.time()
	print(f"Downloaded {len(urls)} sites in {end - start} seconds.\n")