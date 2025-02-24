#Chapter 02-2
#파이썬 완전 기초
#파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type(n)) #type: 자료형 보여줌

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75

# 재선언
var = "Change Value" # 앞에 75로 지정했지만 얘가 덮어씀

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트(int, str 등) class가 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n-> 77
n = 777

print(n,type(n))
print()

m = n
# 777을 m에다가 복사 m->777<-n

#id(identity) 확인: 객체의 고유값 확인

m = 800
n = 655
print(id(m)) # 오브젝트의 고유값
print(id(n))
print(id(m)==id(n))
print()

m = 800
n = 800
# 보기에는 두 개를 설정했지만 파이썬 엔진이 알아서 하나만 만
# 같은 오브젝트 참조

print(id(m)) # 오브젝트의 고유값
print(id(n))
print(id(m)==id(n))
print()

# 다양한 변수 선언
# Camel Case : numberofCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class - 변수 선언 x
# Snake Case : number_of_college_graduates -> 변수 선언에 많이 씀

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
_age = 7
# 숫자와 대부분의 특수문자로 시작 안됨

#예약어는 변수명으로 불가능
# for, as, class
# 인터넷: python reserved words 쳐보면 알 수 있음
