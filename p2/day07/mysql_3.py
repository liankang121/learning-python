import  pymysql


db = pymysql.connect(host = "127.0.0.1",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "str",
                     charset = "utf8")
cur = db.cursor()

try:
    name = input("name:")
    age = input("age")
    gender = input("gender")
    #cur.execute("insert into class(name,age,sex) values ('%s',%d,'%s')"%(name,int(age),gender))
   # cur.execute("insert into class (name,age,sex) values (%s,%s,%s)",[name,age,gender])
    #cur.execute("update class set name= 'sbn' where id = 2")
    cur.execute("delete from class   where id = 5")
except Exception as e:
    db.rollback()
    print(e)

db.commit()
cur.close()
db.close()
#%(name,int(age),gender)