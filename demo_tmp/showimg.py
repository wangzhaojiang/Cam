#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author: wangzhaojiang
# Created Time: 2014年07月14日 星期一 19时57分11秒

import cv2

path = raw_input('Enter the file : ')

img = cv2.imread(path)
cv2.namedWindow("image")
cv2.imshow("image", img)
print img
cv2.waitKey(0)
cv2.destroyAllWindows()
