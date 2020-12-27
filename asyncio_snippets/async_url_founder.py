
""" Web Crawler - Get asyncronously links(urls) embedded in different HTML pages """

import pathlib
import asyncio
import aiohttp
import aiofiles
import re


async def fetch_html(session, url) :
    """GET request wrapper to fetch page HTML."""
    response = await session.request(method="GET", url=url)
    html = await response.text()
    return html


async def parse_url(session, url):
    """Find and parse hrefs in the HTML of url"""
    html = await fetch_html(session, url)
    HREF_RE = re.compile(r'href=".*?"')
    found_links = set()
    for link in HREF_RE.findall(html):
        found_links.add(link)
    print(f"URL - {url} - done : {len(found_links)}")
    return found_links


async def write_links(session, url):
    """Collect links/hrefs from url and write them to file"""
    found_links = await parse_url(session, url)
    if not found_links:
        return None
    here = pathlib.Path(__file__).parent
    async with aiofiles.open(here.joinpath("foundurls.txt"), "a") as f:
        for link in found_links:
            await f.write(f"{url}\t{link}\n")


async def bulk_crawl_and_write(urls):
    """Crawl and write concurrently to file for multiple urls"""
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[write_links(session, url) for url in urls])


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))
        #urls = infile.readlines()

    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")
        outfile.close()

    asyncio.run(bulk_crawl_and_write(urls))
