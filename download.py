import json
import logging
import os
from pathlib import Path
import urllib.request
from urllib.request import urlopen, Request
import requests
import mysql.connector
import configparser
import os.path
from os import path

config = configparser.ConfigParser()
config.read('config.ini')
cnx = mysql.connector.connect(
    user=config['mysqlDB']['user'],
    password=config['mysqlDB']['password'],
    host=config['mysqlDB']['host'],
    database=config['mysqlDB']['database']
)

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}


def get_links(page , keyword):
    req = Request(
        "https://api.500px.com/v1/photos/search?type=photos&term="+keyword+"&image_size[]=2048&formats=jpeg&include_tags=true&watermark=false&page=" + str(
            page) + "&rpp=50", method='GET')
    FinalData = []
    with urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        if len(data['photos']) != 0:
            for element in data['photos']:
                Data = {
                    'id': element['id'],
                    'ImageUrl': element['image_url'][0],
                    'Name': element['name'],
                    'Description': element['description'],
                    'Category': element['category'],
                    'Tags': element['tags'],
                    'Data': {
                        'ShutterSpeed': element['shutter_speed'],
                        'FocalLength': element['focal_length'],
                        'Aperture': element['aperture'],
                        'Camera': element['camera'],
                        'Lens': element['lens'],
                        'Iso': element['iso'],
                        'TakenAt': element['taken_at']
                    }
                }
                FinalData.append(Data)
            return FinalData
        else:
            return False


def download_link(directory, link, name):
    download_path = directory / os.path.basename(str(name) + '.jpg')
    f = open(download_path, 'wb')
    f.write(requests.get(link).content)
    f.close()
    logger.info('Downloaded %s', link)


def download_link2(directory, Link):
    download_path = directory / os.path.basename(str(Link['id']) + '.jpg')
    if not path.exists(download_path):
        f = open(download_path, 'wb')
        f.write(requests.get(Link['ImageUrl']).content)
        f.close()
        insertToDb(Link, download_path)
        logger.info('Downloaded %s', Link['ImageUrl'])
    else:
        logger.info('File Exist %s', Link['ImageUrl'])


def insertToDb(Link, LocalLink):
    qry = (
        "INSERT INTO `images`(`id`, `Name`, `OrginalLink`,`LocalLink`, `Description`,  `Category`, `Tags`, `Data`) VALUES ( %s, %s, %s,%s, %s, %s, %s, %s)")
    Datas = (Link['id'], Link['Name'], Link['ImageUrl'], str(LocalLink), Link['Description'], Link['Category'],
             str(Link['Tags']), str(Link['Data']))
    cursor = cnx.cursor()
    cursor.execute(qry, Datas)
    cnx.commit()


def setup_download_dir():
    download_dir = Path('Images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir
