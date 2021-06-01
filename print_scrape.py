from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, "html.parser")

csv_file = open('cms_scrape69.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

#article = soup.find('article')
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print("Headline: " + headline)

    summary = article.find('div', class_='entry-content').p.text
    print("Summary: " + summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    print("Video ID: " + vid_id)
    yt_link = f'https://youtube.com/watch?v={vid_id}'

    print("You-Tube Link: " + yt_link)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
    
