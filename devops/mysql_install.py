import os
import sys

url = 'https://dev.mysql.com/get/Downloads/MySQL-5.6/MySQL-client-5.6.47-1.el7.x86_64.rpm'
mysql_client=os.path.basename(url)
cmd1 = 'wget ' + url
res1 = os.system(cmd1)

if res1 != 0:
    print('failed1')
    sys.exit(1)

cmd2 = 'rpm -ivh --nodeps --force ' + mysql_client
res2 = os.system(cmd2)
if res2 != 0:
    print('failed2')
    sys.exit(1)




