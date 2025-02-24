# chapter03_05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'Kim', 'phone': '01012341234', 'birth': '870514'} # 키: 값(밸류)
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', '33'),
    ('Grade', 'A'),
    ('Status', True)
]) # 리스트 안에 튜플 형태로 넣을 수도 있음, 그러나 불편
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
) # 이런 방법도 ~

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print() # 이거 하는 이유가 뭔데...

# 출력
print('a - ', a['name']) # 존재x -> 에러 발생
print('a - ', a.get('name')) #존재x -> none 처리: 따라서 겟이 더 안전
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ' , f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a -', a)
a['rank'] = [1, 2, 3]
print('a -', a)

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items: 반복문(___iter___)에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())

print()

print('a - ', a.items()) # item에서는 둘 다 나옴
print('a - ', b.items())
print('a - ', c.items())

print('a - ', list(a.items())) # 형변환 가능
print('b - ', list(b.items()))

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem()) # 순서가 없으므로 무작위로 꺼내보는 것
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
# 빈 딕셔너리 되면 뒤에꺼가 실행 안 됨

print()

print('a -', 'birth' in a)
print('d - ', 'City' in d)

# 수정
a['test'] = 'test_dict'
print('a-', a)

a['address'] = 'dj' # 바꾸면 자도으로 수정됨
print('a- ', a)

a.update(birth = '910904') # 업데이트 메소드 사용하면 조금 더 엄밀
print('a- ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a-', a)
