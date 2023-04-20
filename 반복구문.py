#개수를 모르는 경우
value = 5 
while value > 0:
    print(value)
    value -= 1 

#개수를 알고 있는 경우
lst = [100,200,300]
fruit = {"apple":10, "banana":20, "kiwi":30}
for item in fruit.items():
    print(item)

#특정 조건에서 탈출
print("---break---")
lst = list(range(1,11))
print( lst )
for i in lst:
    if i > 5:
        break 
    print("item:{0}".format(i))

#특정 조건은 스킵
print("---continue---")
lst = list(range(1,11))
print( lst )
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))