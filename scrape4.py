from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests

url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing page
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div",{"class":"item-container"})

print(len(containers))

#print(containers[0])
