# Chapter 04-3
# 파이썬 반복문
# while문 실습

# while <expr>:
# <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n)
    n = n - 1

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop()) # last in first count

# 예제3
# break, continue를 만나면 while 문의 처음으로 돌아감
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# 예제 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

# if 중첩
# 예제 5
i = 1
while i <=10:
    print('i:', i)
    if i == 6:
        break
    i += 1

# while-else 구문
# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'qux'
i = 0

while i < len(a): # 4
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list.')
# s = kim일 경우 else 구문 실행됨

# 무한반복 조심해야함
# while True:
# print ('foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())
    # 네 번째 실행될 때 break를 만남
