#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月17日 星期四 10时10分28秒

import cv2
import numpy as np
from socket import *

HOST = '127.0.0.1'
PORT = 10000
ADDR = (HOST, PORT)

cli = socket(AF_INET, SOCK_DGRAM)

cli.sendto('test', ADDR)

data, addr = cli.recvfrom(1024)

data = np.frombuffer(data, dtype = 'uint8')

text = cv2.imdecode(data, 1)

print data

print type(data)

cv2.imshow('frame', data)
cv2.waitKey(0)
data = np.fromstring(data, dtype = 'uint8')
