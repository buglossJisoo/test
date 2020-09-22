#Section02-1
#파이썬 기초코딩
#Print 구문의 이해

#기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

#Separator 옵션 사용

print('T','E','S','T',sep='')
print('2019','02','19', sep='-')
print('nicema','google.com',sep='@')

#end 옵션 사용
#끝부분을 다음과 연결
print('Welcome To',end='') # 문구를 뜨이ㅓ쓰기 해주거나
print(' the black parade',end=' ') #end를 공백처리 하거나
print('piano notes')

print() # 줄바꿈

#format 사용 [], {}, ()
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print('{a} and {b}'.format(a='You', b= 'Me'))

 # %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" %('Jisoo', 5))

print("Test1: %5d, Price: %4.2f" % (773, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776,6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776,b=6534.123))


"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
# \ 이거 다음에잇는표현들을 그래도 표현해줌
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n\n\n')
print('\t\t\ttest')