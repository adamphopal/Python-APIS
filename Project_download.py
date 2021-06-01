import requests
import os
import bs4

url = 'http://xkcd.com' #Starting url
os.makedirs('xkcd', exist_ok=True)  #Store comics in ./xkcd

while not url.endswith('#'):
    #Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find the comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
<img data-aria-label-part="" src="https://pbs.twimg.com/media/DjuKKqPVAAAkise.jpg" alt="" style="width: 100%; top: -11px;">
stream-item-tweet-1025565271447293952