# ctrl + shift + b = 실행
# Chapter02-1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Hello World!')
print()
print("Hello World!")
print('''Hello World!''')
print("""Hello World!""")

# separator 옵션
print('P', 'Y', 'T','H','O','N', sep=' ')
print('010', '1214', '1234', sep='-')

# end 옵션 - 한 줄로 이어주는 역할
print('Welcome to', end=' ')
print('IT NEws', end=' ')
print('Web')

# file 옵션
import sys
#보라색은 예약어이므로 변수지정 불가능
# print('Learn Python', file='test.txt')
# ''앞의 내용을 파일 test에 쓴다는 뜻
print('Learn Python', file=sys.stdout)
#sys 콘솔 아웃이라는 의미
print()

# format 사용(d = 정수, s = 문자열, f = 실수 3.14)
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
#둘 다 같은 결과 출력 - 두번째껀 포맷 함수가 내부적으로 처리, 유연
print('{1} {0}'.format('one', 'two'))
#중괄호 안의 숫자는 순서 의미. 0 1 2... 이런 식
print()

# %s
print('%10s' % ('nice'))
#10이 의미하는 것: 자릿수 - 남은 자릿수에 nice를 넣고 왼쪽부터 공백 처리
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
#음수가 나왔을 때 / 부등호 없을 때는 오른 쪽을 공백으로 채움

print('{:_>10}'.format('nice'))
#부등호 앞 원하는 기호로 공백을 채울 있음
print('{:^10}'.format('nice'))
# 중앙 정렬

print('%5s' % ('nice'))
# 공간 5개 확보
print('%5s' % ('pythonstudy'))
# 이건 5개 이상 문자이므로 그대로 출력

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
# 점이 있으면 절삭
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%f' % (3.1414141414))
print('{:f}'.format(3.1414141414))
print('%02.4f' % (3.141592653589793))
#정수부 여섯자리, 소수부 두자리, 총 자릿수는 여섯자리(아마 정수 기준인듯?)이므로 나머지는 0으로 채
print('{:06.2f}'.format(3.141592653589793))
