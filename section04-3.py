# Section 04-3
# 파이썬 데이터 타임(자료형)
# 리스트, 튜플

# 리스트 (순서O, 중복O, 수정O, 삭제O) 

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'Banana', 'Orange']
e = [10, 100, ['pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d) # 하나의 리스트로 만들어줌
print(c * 3)
print(str(c[0])+ 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c'] # 하나의 인덱스잡고서 하면 리스트자체가 들어감
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # append : 끝부분에 삽입
print(y)
y.sort() # sort : 오름차순 정렬
print(y)
y.reverse() # reverse : 내림차순 정렬
print(y)
y.insert(2,7) # insert(a,b) : a번자리에 b를 넣을꺼야
print(y)
y.remove(2) # remove(b) : b라는 값 지우기
y.remove(7)
# del y[b] : b번 자리에있는 값 지우기
print(y)
y.pop() # pop : 맨 마지막에있는 값을 꺼낸다.
print(y) # LIFO
ex = [88, 77]
#y.append(ex) # append는 list 자체를 삽입
# [88, 77] 이거 자체가 들어감
y.extend(ex) # extend는 ex에있는 값들이 삽입
# 88 77
print(y)

# 삭제 : del, remove, pop //pop은 언젠가 계속 쓰면 error

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b= (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][0])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()
print()

# 튜플 함수

z = (5, 2, 1, 3, 1)
print(z)
print(3 in z)
print(z.index(5)) # index(a) : a라는 값의 index 번호 return
print(z.count(1)) # count(a) : a라는 값 몇개 있어?






