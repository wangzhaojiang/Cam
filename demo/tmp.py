#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月17日 星期四 09时59分20秒

import cv2
from socket import *

cap = cv2.VideoCapture(0)


sock = socket(AF_INET, SOCK_DGRAM)

while (cap.isOpend()):
	t, frame = cap.read()
	ser.sendto(frame, addr)

cap.release()
cv2.destoryAllWindows()
