# Chapter 04_02
# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for v1 in range(10): # 0 ~ 9
    print('v1 is :', v1)

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)

for v3 in range(1, 11, 2):
    print('v3 is :', v3)

# 1 ~ 1000 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v # sum1 = sum1 + v 와 같은 뜻

print('1~1000 Sum : ', sum1)
print('1~1000 Sum : ', sum(range(1, 1001)))
print(type(range(1,11)))
print('1~1000 4의 배수의 합: ', sum(range(4, 1001, 4)))

# Iterables(반복할 수 있는 개체) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리) for 문 사용가능
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
# 리스트 형태도 뒤에 'names'를 붙이면 안에 원소 사용할 수 있음
## for 뒤에 문자는 임의로 설
for n in names:
    print('You are:', n)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]
# int 도 가능
for n in lotto_numbers:
    print("Current number : ", n)

# 예제3
word = "Beautiful"

for s in word:
    print('word :', s)

# 예제4
my_info = {
    "name" : 'Lee',
    "Age" : 33,
    "City" : "Seoul"
}

for value in my_info:
    print('value :', my_info[value])
# 여기서 키는 어떻게 가져옴 ???
for v in my_info.values():
    print('value :', v)

# 예제 5
name = 'FineAppLE'

for n in name:
    if n.isupper(): # 대문자일 경우 그냥 n 출력
        print(n)
    else: # 소문자일 경우 n을 upper 함수로..
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2 ,33 ,15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print('Found : 34!')
        break # 34를 찾으면 for 문을 즉시 빠져나감
    else:
        print('Not found: ', num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)] # 숫자모형 스트링만 보여주고 싶 #
for v in lt:
    if type(v) is bool: # boolean 형일 때는 continue를 만나 print를 하지않고 건너뜀
        continue
    print("current type:", v, type(v))
    print("multiply by 2", v*3)

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2 ,33 ,15, 34, 36, 38]
for num in numbers:
    if num == 24:
        print("Found : 24")
        break
else: # for문이 break를 만날 경우 실행되지 x
    print('Not Found: 24') # 그 때 else 마지막으로 하나 번 실행됨

# 구구단 출력 - 중첩 for 문
for i in range(2,10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end = '') #네자리 정수형
    print() # 줄바꿈 처리

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) #집합은 순서가 x!
