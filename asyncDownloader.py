import asyncio
import logging
import os
from time import time

import aiohttp
import requests

from download import setup_download_dir, get_links

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def async_download_link(directory, link, name):
    download_path = directory / os.path.basename(str(name) + '.jpg')
    f = open(download_path, 'wb')
    f.write(requests.get(link).content)
    f.close()
    logger.info('Downloaded %s', link)


# Main is now a coroutine
async def main():
    download_dir = setup_download_dir()
    # We use a session to take advantage of tcp keep-alive
    # Set a 3 second read and connect timeout. Default is 5 minutes
    page = 1
    while True:
        links = get_links(page)
        if links == False:
            break
        async with aiohttp.ClientSession(conn_timeout=3, read_timeout=3) as session:
            tasks = [(async_download_link(download_dir, l['ImageUrl'], l['id'])) for l in links]
            # gather aggregates all the tasks and schedules them in the event loop
            await asyncio.gather(*tasks, return_exceptions=True)
        links.clear()
        page += 1


if __name__ == '__main__':
    ts = time()
    # Create the asyncio event loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        # Shutdown the loop even if there is an exception
        loop.close()
    logger.info('Took %s seconds to complete', time() - ts)
