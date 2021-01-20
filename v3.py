import logging
import os

from redis import Redis

from rq import Queue

from download import setup_download_dir, get_links, download_link2

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    download_dir = setup_download_dir()
    page = 1
    keyword = input('Enter Your KeyWord : ')
    while True:
        links = get_links(page, keyword)
        if links == False:
            break
        q = Queue(connection=Redis(host='127.0.0.1', port=6379))
        for link in links:
            q.enqueue(download_link2, download_dir, link)
        links.clear()
        page += 1


if __name__ == '__main__':
    main()
