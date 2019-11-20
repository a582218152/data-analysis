import pymysql

db = pymysql.connect('localhost','root','Aa582218152.','study')
cursor = db.cursor()

sql = """create table invoke (
            id int(11),
            name varchar(25),
            salary float)"""

cursor.execute(sql)

db.close()

