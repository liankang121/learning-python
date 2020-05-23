import pymysql

db = pymysql.connect(host = "127.0.0.1",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "str",
                     charset = "utf8")

cur = db.cursor()
while True:
    print("1. sign in ")
    print("2. sign up ")
    select_one = input("请选择：")
    if select_one == "1":
        user = input("user:")
        password = input("password:")
        sql = "select user,password from user_info where user = %s "
        cur.execute(sql,[user])
        res = cur.fetchone()
        print(res)
        if res is  None :
            print("没有此人")
            continue
        else:
            if res[1] == password:
                print("success")

                break
    else:
        user = input("user:")
        password = input("password:")
        sql = "select user,password from user_info where user = %s "
        cur.execute(sql, [user])
        res = cur.fetchone()
        print(res)
        if res == 0:
            sql = "insert into user_info (user,password) values (%s,%s) "
            try:
                res = cur.execute(sql, [user,password])
                db.commit()
            except Exception as e:
                print(e)
                db.rollback()
            print("创建成功")
            break
        else:
            continue

cur.close()
db.close()


