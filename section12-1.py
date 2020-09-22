# Section12-1
# 파이썬 데이터 베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime


# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)


# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)


# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('D:/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))


# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
# \ : 다음문장 이어지게~
c.execute("CREATE TABLE IF NOT EXISTS users(id INTERGER PRIMART KEY, username text, \
email text, phone text, website text, regdate text)")


# 데이터 삽입
# ? 에 값 넣기
c.execute("INSERT INTO users VALUES(1, 'Choi', 'choi@naver.com', '010-3333-3333', \
      'jisoo.com',?)",(nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",
(2,'Park','Park@daum.net','010-1111-1111','Park.com',nowDatetime))


# Many 삽입(튜플, 리스트)
userList = (
    (3,'Lee', 'Lee@naver.com', '010-222-222', 'Lee.com', nowDatetime),
    (4,'Cho', 'Cho@naver.com', '010-555-222', 'Cho.com', nowDatetime),
    (5,'Yoo', 'Yoo@naver.com', '010-6666-111', 'Yoo.com', nowDatetime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
VALUES (?,?,?,?,?,?)",userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# 몇개 삭제 했는지
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)


# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()


# 롤백
# conn.rollback()

# 접속 해제
conn.close()





