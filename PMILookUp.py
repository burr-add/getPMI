import requests as rs

from bs4 import BeautifulSoup

page = rs.get('https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/pmi'
              '/december')
soup = BeautifulSoup(page.content, 'html.parser')
headline = soup.find_all('h1')[0].get_text()

print(headline)
