# -*- Ccoding: utf-8 -*-

import os,sys
import time
import sys 
import pycurl

URL="www.baidu.com"
c = pycurl.Curl()   #创建一个Curl对象
c.setopt(pycurl.URL, URL)
c.setopt(pycurl.CONNECTTIMEOUT, 5)    #定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT, 5 )          #定义请求超时时间
c.setopt(pycurl.NOPROGRESS, 1)        #屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE, 1)      #完成交互后强制断开连接，不重用
c.setopt(pycurl.MAXREDIRS, 1)         #指定http重定向最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)#设置保存DNS信息为30s

#创建一个文件对象，以wb方式打开，用来存储返回的http头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()
except Exception,e:
    print "connection error:" + str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
#PRETRANSFER_TIME = c.getinfo(c.getinfo.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)


TOTAL_TIME = c.getinfo(c.TOTAL_TIME)     #获取传输总时间
HTTP_CODE = c.getinfo(c.HTTP_CODE)            #获取http状态码
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)    #获取下载数据包下载
HEADER_SZIE = c.getinfo(c.HEADER_SIZE)        #获取http头部大小
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)  #获取平均下载速度

#打印输出相关数据 
print "http状态码: %s" % (HTTP_CODE)
print "DNS解析时间: %.2f ms" % (NAMELOOKUP_TIME)
print "建立连接时间: %.2f ms" % (CONNECT_TIME*1000)
#print "准备传输时间: %.2f ms" % (PRETRANSFER_TIME*1000)
print "传输开始时间: %.2f ms" % (STARTTRANSFER_TIME*1000)
print "传输结束总时间: %.2f ms" % (TOTAL_TIME*1000)
print "下载数据包大小: %d bytes/s" % (SIZE_DOWNLOAD)
print "http头部大小: %d byte" % (HEADER_SZIE)
print "平均下载速度: %d bytes/s" % (SPEED_DOWNLOAD)

indexfile.close()
c.close


