import pymysql
#import datetime
#day = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#参数值插入时间
con = pymysql.connect('localhost','root','Aa582218152.','study')
if con:
    print("ok")
    cur = con.cursor()
    if cur:
        list1 = [('qew','njnn','qwqw'),('www','zzz','eee')]

        sql_entry = "INSERT IGNORE INTO aha VALUES(%s,%s,%s)"
        cur.executemany(sql_entry, list1)
        con.commit()
        print("ok1")
    else:
        print("fail1")
    cur.close()
else:
    print("faid2")
con.close()

