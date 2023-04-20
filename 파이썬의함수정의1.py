#리턴하지 않는 경우
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:", x)
#호출
retValue = setValue(5)
print( retValue )

#다중의 값을 리턴하는 경우
def swap(x,y):
    return y,x 
#호출
print( swap(3,4) )

#스코핑룰(이름 해석 규칙)
x = 1 
def func1(a):
    return x+a 
#호출
print( func1(1) )

def func2(a):
    x = 5 
    return x+a
#호출
print( func2(1) )

#함수의 기본값
def times(a=10,b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL
#호출
print( connectURI("naver.com", "80") )
print( connectURI(port="8080", server="daum.net") ) 

#가변인자(갯수가 정해져 있지 않은경우)
def union(*ar):
    res = []
    for item in ar:
        for x in item:
            if x not in res:
                res.append(x)
    return res 

print( union("HAM","SPAM") )
print( union("HAM","SPAM","EGG") )

#람다 함수 정의
g = lambda x,y:x*y
print( g(2,3) )
print( g(3,5) )
print( (lambda  x:x*x)(3) )
print( globals() )

#필터링하는 함수
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)
#조건에 해당하는 함수
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)
print("==람다함수정의==")
iterL = filter(lambda i: i>20, lst)
for item in iterL:
    print(item)