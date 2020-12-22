import bs4
import requests
url = 'https://cricketexchange.in/live'
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
print (soup.prettify())
for para in soup.find_all ('a'):
    print(para.text)
    for links in soup.find_all ('a'):
        links = links.get ('href')
        print(links)

