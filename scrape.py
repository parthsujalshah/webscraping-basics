from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

# print(soup) # normal unformatted html
# print(soup.prettify()) # formatted html
match = soup.find('div', class_='footer')
print(match)

article = soup.find('div', class_='article')
print(article)


articles = soup.find_all('div', class_='article')
for article in articles:
  headline = article.h2.a.text
  print(headline)
  summary = article.p.text
  print(summary)
  print()
