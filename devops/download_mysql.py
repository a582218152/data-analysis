# -*- coding: UTF-8 -*-
import os
import sys

#centos7需先删除mariadb


url_server = 'https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-server-5.6.47-1.el7.x86_64.rpm'
url_client = 'https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-client-5.6.47-1.el7.x86_64.rpm'
#server端
mysql_server=os.path.basename(url_server)
download_mysql_server = 'wget ' + url_server
res2 = os.system(download_mysql_server)
if res2 != 0:
    print("failed")
    sys.exit(1)
#client端下载
mysql_client=os.path.basename(url_client)
cmd1 = 'wget ' + url_client
res1 = os.system(cmd1)

if res1 != 0:
    print('failed1')
    sys.exit(1)
#安装协调文件
cmd4 = 'yum install -y autoconf'
os.system(cmd4)
#解压server
cmd3 = 'rpm -ivh --nodeps --force ' + mysql_client
res3 = os.system(cmd3)
if res3 !=0:
    print("解压client失败")
    sys.exit()
#解压server
cmd2 = 'rpm -ivh --nodeps --force ' + mysql_server
res2 = os.system(cmd2)
if res2 != 0:
    print('解压server失败')
    sys.exit(1)

#打开某个文件拿取字符

with open('/root/.mysql_secret') as f:
  m = f.readlines()
  object = m[0]
  mysql_serect = object.split()[-1]

  print("数据库的随机密码是:%s" % mysql_serect  )    #格式化输出、占位符%s表示字符串，%d表示十进制数字

#启动mysql

mysqld_start = 'systemctl start mysql'
os.system(mysqld_start)
netstat_show = 'ss -ntpl'
os.system(netstat_show)
#判断服务是否正常启动









