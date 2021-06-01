from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://miakhalifa.com/home').text

soup = BeautifulSoup(source, "html5lib")

csv_file = open('riley.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

article = soup.find('article')


for article in soup.find_all('article'):
#    headline = article.h2.a.text
#    print(headline)

 #   summary = article.find('div', class_="video-title ellipsis").p.text
  #  print(summary)

    try:
        vid_src = article.find('iframe', class_='videoLis')['href']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        print(vid_id)


        yt_link = f'http://miakhalifa.com/home?aid=pornhub&prg=pps&cmp=PsProfile{video_link}'
    except Exception as e:
        yt_link = None


        print(yt_link)

        print()

        csv_writer.writerow([headline, summary, yt_link])

csv_file.close()



#https://cdn-statics.cleeng.com/vod-embed/img/bg.png?v=dce8b0437c
