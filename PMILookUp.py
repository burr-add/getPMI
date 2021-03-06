import requests as rs
from datetime import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup

# Establishes valid date range
today = datetime.today()
one_month_ago = (today - relativedelta(months=1)).strftime("%B")
two_month_ago = (today - relativedelta(months=2)).strftime("%B")
three_month_ago = (today - relativedelta(months=3)).strftime("%B")
valid_months = [one_month_ago, two_month_ago, three_month_ago]

# Gets valid month from user input
while True:
    print("Enter month of desired PMI: ")
    PMI_month = input()
    if PMI_month not in valid_months:
        print("Please enter a valid month")
    else:
        break

# Inputs valid month into url to scrape correct site
PMI_url = 'https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/pmi/' + str(PMI_month)
page = rs.get(PMI_url)
soup = BeautifulSoup(page.content, 'html.parser')
headline = soup.find_all('h1')[0].get_text()

print(str(PMI_month)+" "+headline)
