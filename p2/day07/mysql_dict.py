import  pymysql

db = pymysql.connect(host =  "127.0.0.1",
                     port = 3306,
                     user = "root",
                     password= "123456",
                     database = "dict",
                     charset = "utf8")
cur  = db.cursor()
with open("dict.txt","r") as f:
    for line in f:
        word_list = line.split(" ",1)
        try:
            cur.execute("insert into words(word,expl) values(%s,%s)",[word_list[0],word_list[1]])
        except Exception as e:
            db.rollback()
            print(e)
        else:
            db.commit()
cur.close()
db.close()

