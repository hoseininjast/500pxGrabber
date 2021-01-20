from selenium import webdriver
import mysql.connector
import configparser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

config = configparser.ConfigParser()
config.read('config.ini')
cnx = mysql.connector.connect(
    user=config['mysqlDB']['user'] ,
    password=config['mysqlDB']['password'],
    host=config['mysqlDB']['host'],
    database=config['mysqlDB']['database']
)
#
#
#
# def InsertToDataBase(ID,Name,OrginalLink,LocalLink,Description,Category,Tags,Data):
#     qry = (
#         "INSERT INTO `images`(`id`, `Name`, `OrginalLink`,`LocalLink`, `Description`, `Tags`, `Category`, `Data`) VALUES ( %s, %s, %s,%s, %s, %s, %s, %s)")
#     Datas = (ID, Name, 'OrginalLink','LocalLink',Description, Category, Tags, Data)
#     cursor.execute(qry, Datas)
#     cnx.commit()
#
# cursor = cnx.cursor()
#
# InsertToDataBase()
# cursor.close()
# cnx.close()
#
#




# https://api.500px.com/v1/photos/search?type=photos&term=benz&image_size%5B%5D=1&image_size%5B%5D=2&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35&image_size%5B%5D=36&image_size%5B%5D=2048&image_size%5B%5D=4&image_size%5B%5D=14&include_states=true&formats=jpeg%2Clytro&include_tags=true&exclude_nude=true&page=3&rpp=50




Keyword = input("Enter your Keyword: ")

driver = webdriver.Firefox()
driver.get("https://500px.com/search?submit=Submit&q="+Keyword+"&type=photos")
elements = driver.find_elements_by_css_selector("div.photo_thumbnail a.photo_link ")
for element in elements:


    print(element.get_attribute("href"))
# images = driver.find_elements_by_tag_name('img')
# for image in images:
#     print(image.get_attribute('src'))

driver.close()