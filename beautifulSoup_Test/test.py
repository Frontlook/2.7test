from urllib import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html, 'lxml')

for child in bsObj.findAll("img",{"src":re.compile(r'../img/gifts/img..jpg')}):
    print child.attrs["src"]
