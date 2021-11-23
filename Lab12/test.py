import requests
import bs4
#URL = 'http://mike.cpe.ku.ac.th/'
URL = 'http://earth.mikelab.net:8080/~std50/'
HEADER = {'User-Agent': 'Kun toto,std80,toto@ku.th'}
response = requests.get(URL, headers=HEADER)
response.encoding = 'utf-8'
page = response.text
html_page = bs4.BeautifulSoup(page, 'html.parser')
myname = html_page.find_all(id='myname')
myname_th = html_page.find_all(id='myname_th')
print(myname[0].text)
print(myname_th[0].text)
my_listkeys = html_page.find_all('th')
my_listvalues = html_page.find_all('td')
for i in range(len(my_listkeys)):
  print(f'{my_listkeys[i].text.strip()}: {my_listvalues[i].text}')
a = html_page.find_all(class_='buttonC')
print(a)