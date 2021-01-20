import logging
import os
from time import time

from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    ts = time()
    download_dir = setup_download_dir()
    page = 1
    while True:
        links = get_links(page)
        if links == False:
            break
        for link in links:
            download_link(download_dir, link['ImageUrl'] , link['id'])
        logging.info('Took %s seconds', time() - ts)
        links.clear()
        page += 1


if __name__ == '__main__':
    main()
