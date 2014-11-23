#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月17日 星期四 09时59分20秒

import cv2
from socket import *
import numpy as np

cap = cv2.VideoCapture(0)

t, frame = cap.read()

ser = socket(AF_INET, SOCK_DGRAM)
ser.bind(('', 10000))

print 'waiting'
data, addr = ser.recvfrom(1024)
print data

ret, data = cv2.imencode('.jpg', frame, [1, 80])

print data
#data = numpy.array(data)
data = data.data
#data = data.tostring()
#print data
print type(data)

#data = cv2.imdecode(text, 1)
#print data
ser.sendto(data, addr)

data = np.fromstring(data, dtype = 'uint8')

t = cv2.imdecode(data, 1)
print data

cv2.imshow('frame', data)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
