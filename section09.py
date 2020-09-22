# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로

# 파일 읽기
# 예제1
f = open('./resource/review.txt','r')
content = f.read()
print(content)
print(dir(f)) # f의 속성값들이 나와있음.
# 반드시 close 리소스 반환
f.close()

print('--------------------')

# 예제2
# with문은 close 안써줘도 된다.
with open('./resource/review.txt','r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('--------------------')
print('--------------------')

# 예제3
with open('./resource/review.txt','r') as f:
    for c in f:
        print(c.strip())


print('--------------------')
print('--------------------')

# 예제4
with open('./resource/review.txt','r') as f:
    content = f.read()
    print('>', content)
    content = f.read() # 내용 없음
    print('>', content) 

print('--------------------')
print('--------------------')

# 예제5 
# 한줄씩 출력
with open('./resource/review.txt','r') as f:
    line = f.readline()
   # print(line)
    while line:
       print(line, end=' #### ')
       line = f.readline()

# 예제6 
# 리트스 / 리스트단위로 읽기
with open('./resource/review.txt','r') as f:
    contents = f.readlines()
    print(contents) # 리스트로 출력
    for c in contents:
        print(c, end = ' *****')

print('--------------------')
print('--------------------')


# 예제7
score = []
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line))
    print(score)

# {:6.3} : 6자리고 소수점 셋째자리
print('Average : {:6.3}'.format(sum(score)/len(score)))
    

# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('Nicewoman!\n')


# 예제2
# append
with open('./resource/text1.txt','a') as f:
    f.write('Goodwoman!\n')

# 예제3
from random import randint

with open('./resource/text1.txt','w') as f:
    for cnt in range(6): # 6번 반복
        f.write(str(randint(1,50))) # 0~50이하
        f.write('\n')


# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text1.txt','w') as f:
    list = ['Kim\n','Oark\n','Choi\n']
    f.writelines(list)

# 예제5
# 파일에 쓰는거 print문으로도 가능
with open('./resource/text1.txt','w') as f:
    print('Test contests1!', file=f)
    print('Test contests2!', file=f)