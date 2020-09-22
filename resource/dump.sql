BEGIN TRANSACTION;
CREATE TABLE users(id INTERGER PRIMART KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Choi','choi@naver.com','010-3333-3333','jisoo.com','2020-07-18 21:02:06');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2020-07-18 21:02:06');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-222-222','Lee.com','2020-07-18 21:02:06');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-555-222','Cho.com','2020-07-18 21:02:06');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-6666-111','Yoo.com','2020-07-18 21:02:06');
COMMIT;
