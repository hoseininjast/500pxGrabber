import requests
import json

from bs4 import BeautifulSoup

from urllib.request import urlopen, Request
from download import get_links



# page = 1
# req = Request("https://api.500px.com/v1/photos/search?type=photos&term=benz&image_size[]=2048&formats=jpeg&include_tags=true&watermark=false&page="+str(page)+"&rpp=50", method='GET')
# with urlopen(req) as resp:
#     data = json.loads(resp.read().decode('utf-8'))
#     for element in data['photos']:
#         print(element['id'])

# headers = {
#     'authority': 'api.500px.com',
#     'accept': 'application/json, text/plain, */*',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'origin': 'https://500px.com',
#     'referer': 'https://500px.com/',
# }
# imageid = 15599799;
# params = (
#     ('ids', imageid),
#     ('image_size[]', ['1', '2', '32', '31', '33', '34', '35', '36', '2048', '4', '14']),
#     ('include_states', '1'),
#     ('expanded_user_info', 'true'),
#     ('include_tags', 'true'),
#     ('include_geo', 'true'),
#     ('is_following', 'true'),
#     ('include_equipment_info', 'true'),
#     ('include_licensing', 'true'),
#     ('include_releases', 'true'),
#     ('liked_by', '1'),
#     ('include_vendor_photos', 'true'),
# )
# response = requests.get('https://api.500px.com/v1/photos', headers=headers, params=params)
# data  = json.loads(response.content)
# BestImageUrl = data['photos'][str(imageid)]['image_url'][-1]
# filename = str(imageid)
# r = requests.get(BestImageUrl, allow_redirects=True)
# open('Images/'+filename+".jpg", 'wb').write(r.content)
# page = 1
# response = requests.get("https://api.500px.com/v1/photos/search?&term=benz")
# data  = json.loads(response.content)
# print(data['total_pages'])
#
#
#
# while True:
#     response = requests.get("https://api.500px.com/v1/photos/search?type=photos&term=benz&image_size[]=2048&formats=jpeg&include_tags=true&watermark=false&page="+str(page)+"&rpp=50")
#     data = json.loads(response.content)
#     print(page)
#     page += 1
#     if(page > data['total_pages']):
#         break
#


# requests.get('https://api.500px.com/v1/photos', headers=headers, params=params)
