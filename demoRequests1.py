#requests를 사용하면 보다 적은 코드로 웹서버에 대한 
#요청을 처리할 수 있다. 
import requests

r = requests.get('https://brunch.co.kr/')
#정상인 경우 200 출력 
print(r.status_code)
#text/html 
print(r.headers['content-type'])  
#utf-8
print(r.encoding)  
#print(r.text)