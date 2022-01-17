import requests as rs

from bs4 import BeautifulSoup

PMI_month = input("Enter month:")
PMI_url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/pmi/"+str(PMI_month)
page = rs.get(PMI_url)
soup = BeautifulSoup(page.content, 'html.parser')
headline = soup.find_all('h1')[0].get_text()

print(str(PMI_month)+" "+headline)
