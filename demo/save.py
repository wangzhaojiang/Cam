#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月16日 星期三 11时29分11秒

import cv2

cap = cv2.VideoCapture(0)

#fourcc = cv2.VideoWriter_fourcc()
out = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), 20.0, (640,480))

#while(cap.isOpened()):
while True:
	ret, frame = cap.read()
	if ret == True:

		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0XFF == ord('q'):
			break

print type(frame)
cap.release()
out.release()
cv2.destroyAllWindows()
