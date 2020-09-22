# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print('1:',end=' ')

for s in q1.keys():
    if s == '가을':
        print(q1[s])

# for k,v in q1.items():
#     if k == '가을':
#         print(v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print('2:', end=' ')

for k,v in q2.items():
    if v == '사과':
        print(k,v)
        break
else:
    print('사과 없음')

# if q2.get('가을') == "사과":
#     print("사과 있당.")
# else:
#     print("사과 없당.")


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
print('3:', end=' ')
score = 41
if score >=81 :
    print("A학점")
elif score >=61 :
    print("B학점")
elif score >=41 :
    print("C학점")
elif score >=21 :
    print("D학점")
elif score >=0 :
    print("E학점")
else:
    print("존재하지 않는 점수입니다.")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a = 12
b = 6
c = 18
# a, b, c = 12, 6, 18

print('4:', end=' ')

# best = a

# if b > a:
#     best = b
# if c > b:
#     best = c
# print('best : ', best)

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif a > c:
    if a > b:
        print(a)
    else:
        print(b)
elif b > c:
    if b > a:
        print(b)
    else:
        print(a)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-3473837'
print('5:', end=' ')

if s[7]  == '2' or s[7] == '4':
    print("여자입니다.")
elif s[7] == '1' or s[7] == '3':
    print("남자입니다.")


if int(s[7]) % 2 == 0:
    print("여자입니다.")
else:
    print("남자입니다.")


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
print('6:', end=' ')
for s in q3:
    if s == "정":
        continue
    else:
        print(s, end=' ')

print()

# q5 = [x for x in q3 if x != '정']
# print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print('7:',end= ' ')
for s in range(1,101,2):
    print(s , end= ' ')
print()

# print('-----------------------')
# a = [x for x in range(1,101) if x % 2 !=0]
# print(a)

print()



# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

print('8:', end=' ')
for s in q4:
    if len(s) >=5:
        print(s, end= ' ')
    else:
        continue

# print()
# a = [x for x in q4 if len(x) >=5]
# print(a)


print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print('9:', end=' ')
for s in q5:
    if s.islower():
        print(s, end= ' ')
    else:
        continue

# print()
# a = [x for x in q5 if x.islower()]
# print(a)

print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for s in q6:
    if s.islower():
        s.upper()
    else:
        s.lower()

print('10: ', q6)

# print()
# a= [x.upper() if x.islower() else x.lower() for x in q6]
# print(a)

print()

# 리스트 컴프리헨션 (6~10번 주석처리부분 리스트 컴프리헨션으로 코딩한것)
numbers = []

# 일반적인 방법 
for n in range(1,101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션 방법
numbers2 = [x for x in range(1, 101)]
print(numbers2)

# x = [x for x in range(1,101) if 조건문]

