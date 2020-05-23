import  pymysql

db  = pymysql.connect(host = "127.0.0.1",
                      port =3306,
                      user ="root",
                      password = "123456",
                      database = "str",
                      charset = "utf8")
cur = db.cursor()
sql = "select * from class;"
cur.execute(sql)
re = cur.fetchone()

re1 = cur.fetchmany(3)
print(re)
print(re1)
db.commit()
cur.close()
db.close()