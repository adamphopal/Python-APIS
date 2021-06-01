#!/usr/bin/env python3

#Chapter 11 Practice
#Image Site Downloader - Downloads images in an Imgur catagory
#Change URL variable to the Imgur catagory link

import requests
import os
import bs4

url = 'https://twitter.com/JenSelter/media'
os.makedirs('jen', exist_ok=True)

print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
postElem = soup.select('a img')
if postElem == []:
    print('Could not find the posts images.')
else:
    for i in range(0, len(postElem)):
        postUrl = 'https://twitter.com/JenSelter/media' + str(postElem[i].get('src'))
        print('Downloading image %s...' % (postUrl))
        res = requests.get(postUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('jenselter', os.path.basename(postUrl)), 'wb')
        for chunk in res.iter_content(1000000):
            imageFile.write(chunk)
        imageFile.close()

print('Done.')
#https://pbs.twimg.com/media/DjuKKqPVAAAkise.jpg
