#Chapter03-2
#파이썬 문자형
#문자형은 중요!!

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1)) # 길이

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy
print("I'm Boy")
print('I\'m Boy') # 역슬래시 쓰면 뒤의 특수기호 그대로 표시
print('a \t b') # 키보드의 tab 키만큼

escape_str1 = "Do you have \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!" # 줄바꿈

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\tpie_basic\test'
print(raw_s1)

# 멀티라인 입력: 여러 줄에 걸쳐서 한 번에 입력
# 역슬래시 사용
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""

print(multi_str) # ???

#문자열 연산
str_01 = "python"
str_02 = "Apple!"
str_03 = "How are you doing"
str_04 = "Seoul Daejoen Busan Jinju"

print(str_01*3)
print(str_01 + str_02)
print('y' in str_01)
print('n' in str_01)
print('p' not in str_02)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswitch, count, endswitch, isaplpha...)

print("Capitalize: ", str_01.capitalize())
print("endswith?: ", str_02.endswith("!"))
print("replace", str_01.replace("thon", " Good"))
print("sorted: ", sorted(str_01))
print("split: ", str_04.split('!'))


# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) #__iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습
str_sl = "Nice Python"
print(len(str_sl))
print(str_sl[0:3]) #3-1까지 나옴 - 0, 1, 2까지 슬라이싱
print(str_sl[5:]) #[5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11] 11까지 슬라이싱이랑 같은 뜻
print(str_sl[:len(str_sl)-1])
print(str_sl[1:9:2]) # 거꾸로 갈 땐 -1부터 시작 , 바로 갈 땐 0부터
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2]) # 처음부터 끝까지 두 칸 간격으로 가져오기
print(str_sl[::-1])

# 아스키 코드
a = 'z'

print(ord(a))
print(chr(122))
