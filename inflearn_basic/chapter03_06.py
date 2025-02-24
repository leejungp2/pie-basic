# Chapter03_06
# 집합(Set) 특징
# 집합 자료형(순서 x, 중복 x, 추가o, 삭제o)

# 선언
# 중괄호에 키와 밸류가 있다면 딕셔너리, 아니면 집합
a = set() # 빈 집합
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # 중복 데이터는 자동으로 표시하지 않음
f = {42, 'foo'}, (1,2,3), 3.14159

print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)

# 튜플 변환(set -> tuple), 슬라이싱 가능하다는 뜻
t=tuple(b)
print('t-', type(t), t)
print('t-', t[0], t[1:3])

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('1-', l)
print('l2 -', l2)

# 길이
print(len(a)) # 공집합
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

#집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2) # 교집합
print('s1 & s2 :', s1.intersection(s2)) # 교집합 정확하게 함수로

print('s1 | s2 :', s1 | s2) # 합집합
print('s1 | s2 :', s1.union(s2))

print('s1 - s2 :', s1 - s2) # 차집합
print('s1 - s2 :', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 :', s1.isdisjoint(s2)) # 교집합이 있으면 false

# 부분집합 확인
print('subset :', s1.issubset(s2)) # s1이 s2의 부분집합인가?
print('superset :', s1.issuperset(s2)) #s1집합이 s2를 포함하는 집합인가?

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 -', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)
print('s1 -', s1)
s1.discard(7) # 리무브와 달리 에러 발생하지 않음!

s1.clear() # 싹 지우기
print('s1 - ', s1)

a = [1, 2, 3]
print('s1 -', s1)
