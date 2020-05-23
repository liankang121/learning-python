import  pymysql


db = pymysql.connect(host = "127.0.0.1",
                     port = 3306,
                     user = "root",
                     password ="123456",
                     database = "str",
                     charset = "utf8")

cur = db.cursor()
cur.execute("insert into class values (11,'ll',12,'f');")
db.commit()
cur.close()
db.close()

