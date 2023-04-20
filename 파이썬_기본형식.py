# 파이썬_기본형식.py
x = 100
y = 3.14
print( type(x) )
print( type(y) )

strA = "python is very powerful"
strB = "파이썬은 강력해"
print( len(strA) )
print( len(strB) )

strC = """다중 라인으로 저장할 경우
이렇게 묶으면
다중 라인으로 인식합니다."""
print(strC)

#list
lst = [1,2,3,4,5]
print( type(lst) )
print( len(lst) )
print( lst )

#리스트에 입력, 수정, 삭제, 검색하기
lst.append(6)
lst.insert(1,0)
lst[0] = 100
lst.remove(5)
print( lst )

#튜플은 초기화하면 읽기전용으로 사용됩니다.
tp = (100,200,300)
print( len(tp) )
print( tp.index(200) )
print( tp.count(300) )
print("id: %s, name: %s" % ("kim","김유신"))

#함수 정의
def times(a,b):
    return a+b, a*b 
#호출
result = times(3,4)
print( result )
print( result[0] )
print( result[1] )

#한번에 데이터 입력(*은 Tuple을 의미)
args = (5,6)
print( times(*args) )

#set형식
a = {1,2,3,3}
b = {3,4,4,5}
print( a )
print( b )
print( type(a) )
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )

#형식변환(Type casting)
a = set((1,2,3))
print( type(a) )
b = list(a)
b.append(4)
print( b )
c = tuple(b)
print( type(c) )
print( c )
