# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메쏘드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해 # 클래스는 붕어빵 틀, 인스턴스는 객체에 포함
# 클래스 변수는 직접 접근 가능, 인스턴스 변수는 객체 별로 존재

# 예제 1
class Dog: # object 상속받음, object 안 써도 됨
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성 - self 붙은건 나만의 변수라는 뜻
    def __init__(self, name, age): # 클래스로 사용할 변수를 지정할 수 있음
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baaby", 3)

# 비교
print(a == b)

# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}' .format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species) #인스턴스화된 변수로도 접근 가능

# 예제 2
# self의 이해
class SelfTest:
    def func1(): #안에 self가 없는 건 클래스 메쏘드  #init 없으면 파이썬이 내부적으로 알아서 실행해
        print('Func1 called')
    def func2(self):
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

SelfTest.func1() # 매개변수가 없으므로 class에서 직접 호출
# SelfTest.func2() # 예외
SelfTest.func2(f) # self가 붙은건 하나의 매개변수를 사용하는 인스턴스 메쏘드이므로 괄호 안에 f

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    def __del__(self): #소멸
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
print('>>>', user1.stock_num)

# 예제4
class Dog: # object 상속받음, object 안 써도 됨
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성 - self 붙은건 나만의 변수라는 뜻
    def __init__(self, name, age): # 클래스로 사용할 변수를 지정할 수 있음
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('julie', 4)
d = Dog('Mary', 10)
# 메소드 호출
print(c.info())
print(c.speak('Wal Wal'))
