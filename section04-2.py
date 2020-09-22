# Section 04-2
# 문자열, 문자열연산, 슬라이스

str1 = "I am Girl."
str2 = 'NiceWoman'
str3 = ''
str4 = str('ace')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = """ 문자열 멀티라인 테스트"""
print(multi)

multi2 = \
"""
문자열

멀티라인

테스트
"""
print(multi2)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc '
str_o3 = "def"
str_o4 = "Nicewoman"

print(str_o1*100)
print(str_o2 + str_o3)
print(str_o3 * 3)
print('a' in str_o4) # a라는 문자가 str_o4에 포함되어있는가?
print("f" in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77)+  "a")
print(str(10.4)+ 'b')

# 문자열 함수

a = 'nicewoman'
b = 'apple'

print(a.islower())
print(a.endswith("n"))
print(a.capitalize())
print(a.replace('nice','good')) # nice를 good으로 바꾸기
print(list(reversed(b)))

# a = 'nicewoman'
# b = 'apple'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4]) # 처음부터 4전까지
print(a[:]) # 처음부터 끝까지
print(b[0:4:2]) # 2만큼 뛰고서 print
print(b[1:-2]) # 1자리 p부터 시작 -2인 l 전까지 나옴 pp
print(b[::-1]) # 처음부터 끝까지 나오는데 -1부터 거꾸로 출력
