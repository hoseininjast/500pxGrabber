import logging
import os
from multiprocessing import Pool
from queue import Queue
from threading import Thread
from time import time

from functools import partial

from download import setup_download_dir, get_links, download_link2

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    keyword = input('Enter Your KeyWord : ')
    worker = input('Enter Worker Count : ')
    ts = time()
    download_dir = setup_download_dir()
    page = 1
    while True:
        links = get_links(page,keyword)
        if links == False:
            break
        download = partial(download_link2, download_dir)
        with Pool(int(worker)) as p:
            p.map(download, links)
        links.clear()
        page += 1

    logging.info('Took %s seconds', time() - ts)


if __name__ == '__main__':
    main()
