from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # <span class="subject_fixed" data-role="list-title-text" title="로지텍 MX 메카니컬 키보드 청축(볼트 포함)">
	# 						로지텍 MX 메카니컬 키보드 청축(볼트 포함)
	# 					</span>
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                title = item.text.strip() 
                if (re.search('아이폰', title)):
                        print(title)
