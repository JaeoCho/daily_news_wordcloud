import urllib.request
from bs4 import BeautifulSoup
import re
Url = urllib.request.urlopen("https://www.nytimes.com/section/sports")
soup = BeautifulSoup(Url, 'html.parser')

link_list=[]

for link in soup.find_all('a'):
    if "2018/05/31" in link.get('href'):
        if link.get('href') in link_list:
        #print(link.get('href'))
            a=1
        else:
            link_list.append(link.get('href'))

for i in link_list:
    print(i)