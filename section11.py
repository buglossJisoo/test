# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    next(reader) # Header 스킵(1행)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)



# 예제2
with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f,delimiter ='|')
    # delimiter = 'a' : a 문자 기준으로 구분
    next(reader) # Header 스킵(1행)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


# 예제3 (Dict변환)

with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
    print('-------------------------')


# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

# newline='' : 줄바꿈 하지 않겠다.
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f) # 여기서 한번 줄바꿈

    for v in w:
        wt.writerow(v) # 여기서도 한번 줄바꿈
# 두번 줄바꿈 하니까 위에서 newline써줌



# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # for문 안쓰고 모두 출력하기


# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' or 숫자, header = 숫자, skiprow = 숫지ㅏ
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head()) # 상위 5개 출력
print()

# 데이터 확인
print(xlsx.tail()) # 하위 5개 출력

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index = False)
xlsx.to_csv('./resource/result.csv', index = False)
