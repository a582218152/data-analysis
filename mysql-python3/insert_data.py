import pymysql

db = pymysql.connect('localhost','root','Aa582218152.','study')
cursor = db.cursor()

sql = """insert into invoke
          values (1,'jarvis',2500.0),
          (2,'hou',3500.0),
          (3,'ming',4500.0)"""
try:
    cursor.execute(sql)
    db.commit()
    print('go head')
except:
    db.rollback()
    print('fail')
db.close()

