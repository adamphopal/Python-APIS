from urllib.request import urlopen
from bs4 import BeautifulSoup



class Scraper():
    def __init__(self, site):
        self.site = site


        def scrape(self):
                r = urllib.request.urlopen(self.site)
                html = r.read()
                parser = "html.parser"
		#file = open("headlines.txt", "w")
		#response = urlopen(self.site)
		#html = response.read()
                
		soup = BeautifulSoup(html, parser)
		for tag in soup.find_all("a"):
                    url = tag.get("href")
			if url is None:
                            continue
                        if "html" in url:
                            file.write("\n" + url)
				print("\n" + url)
				file.close() 
                            
                        



news = "http://news.google.com/"
Scraper(news).scrape()

#Scraper("http://news.google.com/").scrape()

                   
		
