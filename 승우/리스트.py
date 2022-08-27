#리스트:연속되는 값들을 저장하는변수

# 만드는법
a = [0,10,30,60,80,70]

print(a)

# index: 각각의 리스트 번호
print(a[0],a[2])  #0 30

# 슬라이싱 : 리스트범위
print(a[0:3]) #[0,10,30]
print(a[3:6]) #[60,80,70]
print(a[::-1])#[70,80,60,30,10,0]

#리스트에 들어가는 함수
# 추가,삭제,찾기,갯수
#print(a)
a.append(100) #맨끝에에
a.insert(2,100)
print(a)
del a[2] #리스트에 원하는 번째 삭제
a.pop()  #a.pop() 맨긑에삭제,a.pop(2)리스트의 index가2인 값 삭제
print(a)

#갯수
print(len(a))

#정렬
a. sort()  # 오름차순 으로 정렬
print(a)
a.reverse() #뒤집기 
print(a)


