# -*- coding: utf-8 -*-

import csv
import MySQLdb
import sys
from datetime import datetime, date

input_file = sys.argv[1]
#连接数据库
con = MySQLdb.connect(host='localhost', port=3306,db='my_suppliers',user='root',passwd='Aa582218152')
c = con.cursor()
#向suppliers中插入数据
file_reader = csv.reader(open(input_file,'r'))
header = next(file_reader)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
       if column_index < 4:
         data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
       else:
         a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
# %Y: year is 2015; %y: year is 15
         a_date = a_date.strftime('%Y-%m-%d')
         data.append(a_date)
    print data
    c.execute("""INSERT INTO suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()
print("")

c.execute("SELECT * FROM suppliers")
rows = c.fetchall()
for row in rows:
  row_list_output =[]
  for column_index in range(len(row)):
    row_list_output.append(str(row[column_index]))
    print(row_list_output)

