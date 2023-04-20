# wiki01.py
from bs4 import BeautifulSoup
import urllib.request as req 

#URL주소는 위키문헌에 윤동주를 검색한 결과입니다(한글이 인코딩되어 있습니다). 
url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

#mw-content-text > div
a_list = soup.select(".mw-parser-output > ul > li a")

for a in a_list:
    name = a.string 
    print("-", name)
