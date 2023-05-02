import sqlite3

def getconn():
    conn = sqlite3.connect("c:/green_porject/sqlworks/pydb/memberdb.db")
    return conn
print(getconn(), "연결 객체 생성됨")

def select():
    conn = getconn()
    cursor = conn.cursor()
    sql = "SELECT * FROM member"
    cursor.execute(sql) # 검색 수행
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    conn.close()

def insert():
    conn = getconn()
    cursor = conn.cursor()
    # 동적 바인딩
    sql = "INSERT INTO member(memberid, passwd, name, gender)" \
          "VALUES (?, ?, ?, ?)"
    cursor.execute(sql, ('today123', 'm123456#', '긴하루', '여')) # 검색 수행
    conn.commit() # 커밋 완료
    conn.close()

insert()
select()