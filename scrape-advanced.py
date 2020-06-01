from bs4 import BeautifulSoup
import requests
import csv # saving it in csv file

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('ps_scrape.csv', 'w') # w is for write

csv_witer = csv.writer(csv_file)
csv_witer.writerow(['headline', 'summary', 'video_link'])

# print(soup.prettify())

# article = soup.find('article')
# print(article.prettify())
for article in soup.find_all('article'):

  headline = article.h2.a.text
  print(headline)

  summary = article.find('div', class_='entry-content').p.text
  print(summary)

  try:
    # vid_src = article.find('iframe', class_='youtube-player')
    vid_src = article.find('iframe', class_='youtube-player')['src']
    # print(vid_src)

    vid_id = vid_src.split('/')[4].split('?')[0]
    # print(vid_id) #this is the youtube video id

    yt_link = f'https://youtube.com/watch?v={vid_id}'
  except Exception as e:
    yt_link = None

  print(yt_link)
  print()

  csv_witer.writerow([headline, summary, yt_link])

csv_file.close()