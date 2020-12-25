import concurrent.futures 
import time
import requests
import threading


thread_local = threading.local()


def get_session():
	if not hasattr(thread_local, "session"):
		thread_local.session = requests.Session()
	return thread_local.session


def download_site(site_url):
	print(site_url)
	session = get_session()
	file_name = site_url + '.txt'
	print(file_name)
	with session.get(site_url) as response:
		print(f"Read {len(response.content)} from {site_url}")
		with open(file_name, 'w') as file:
			file.write(response.content)
		file.close()


if __name__ == '__main__':
	start = time.time()

	site_urls = [
	    "https://www.jython.org",
        "http://olympus.realpython.org/dice",
	] * 1

	with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
		executor.map(download_site, site_urls)

	end = time.time()
	print(f'Finished in {end-start} second(s)')