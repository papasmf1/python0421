# cssSelctor01.py
from bs4 import BeautifulSoup

fp = open('c:\\work\\books.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

sel = lambda q:print(soup.select_one(q).string)
sel('#nu')
sel('li#nu')
sel('ul > li#nu')
sel('#bible > #nu')
