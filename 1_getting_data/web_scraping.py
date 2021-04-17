import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/MSFT/balance-sheet?p=MSFT'
page = requests.get(url)
page_content = page.content
soup = BeautifulSoup(page_content, 'html.parser')
table = soup.find_all('div', {'class': "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
for t in table:
    rows = t.find_all('div', {'class': 'D(tbr) fi-row Bgc($hoverBgColor):h'})
    for row in rows:
        print(row.get_text())
