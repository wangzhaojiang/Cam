#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月19日 星期六 19时15分10秒

from socket import *

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(("www.baidu.com", 80))

sock.sendall("GET / HTTP/1.1\r\n\r\n")

while 1:
	data = sock.recv(1024)
	print data
	if not len(data):
		break
