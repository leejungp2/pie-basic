#Chapter03_03
# 파이썬 리스트 = 배열
# 자료구조에서 중요
# 리스트 자료형(순서, 중복, 수정, 삭제 o)

# 선언
a = [] # 빈 리스트 선언 방법
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

#인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0]+d[1]+d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) #e의 -1번째 리스트 안의 1번째
print('e - ', list(e[-1][1])) # 문자열을 리스트 형태로 변환

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>')
print('c+d', c+d)
print('c*3', c*3) # 3이 숫자에 곱해지는 게 아니라 3번 반복
print('Test' + str(c[0])) # c[0]은 원래 숫자형이므로 문자형으로 바꿔줘야 함

# 값 비교
print(c== c[:3] + c[3:]) # 처음부터 3까지, 3부터 끝까지를 더하니까 같
print(c)
print(c[:3] + c[3:])

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c)) # 리스트에서도 하나의 주소값 공유, 같은 곳을 보고 있음

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1:2] = [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
# 슬라이싱 자리를 정해주었을 때는 중첩됨, 범위로 지정하면 원소로 들어감
c[1:3]=[]
print('c - ', c)
del c[2] # 삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a = ', a)
a.append(10) # 데이터의 끝부분에 데이터 삽입할 때 사용
print('a = ', a)
a.sort() # 정렬 - 이 경우 오름차순으로 정렬됨
print('a = ', a)
a.reverse() # 데이터를 반대로
print('a = ', a)
print('a-', a.index(3), a[3])
a.insert(2,7) # 2번째 위치에 7을 넣음
print('a-', a)
a.reverse()
#del a[6]
a.remove(10) # 데이터 그 자체를 삭제
print('a = ', a)
print('a = ', a.pop()) # last in, first out - 가장 마지막 애가 하나씩 빠지는 것
print('a - ', a.count(4)) # 내가 찾는 데이터가 몇 개 있는지
ex = [8,9]
a.extend(ex)
print('a-', a)

# 삭제: remove, pop, del

# 반복문 활용
while a:
    data=a.pop()
    print(data)
    
