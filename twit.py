import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl = "http://www.ucla.edu/"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")
    
print(soup.title.text)
for link in soup.findAll('img'):
    print(link.get('src'))
    
#print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)
#print(soup.find('div',{"class":"react-root"}).('img').text)



