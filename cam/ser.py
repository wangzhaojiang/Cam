#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-23 19:42
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import socket
import cv2
import numpy
import threading

BUFSIZE = 1024

def sock():

    capture = cv2.VideoCapture(0)

    HOST = ''
    PORT = 10000
    ADDR = (HOST, PORT)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen(True)
    print 'listening...'
    while True:
        clisock, addr = s.accept()
        thread = threadcode(clisock, capture)
        thread.start()

class threadcode(threading.Thread):
    def __init__(self, clisock, capture):

        self.clisock = clisock
        self.capture = capture

        threading.Thread.__init__(self)

    def run(self):
        global BUFSIZE
        while True:
            ret, frame = self.capture.read()
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode('.jpg', frame, encode_param)
            data = numpy.array(imgencode)
            stringData = data.tostring()

            if (self.clisock.recv(BUFSIZE) == 'yes'):
                #print len(stringData)
                self.clisock.send(str(len(stringData)).ljust(16))
                self.clisock.send(stringData)
            else:
                break


        #    decimg = cv2.imdecode(data, 1)
        #    cv2.imshow('CLIENT', decimg)

        #    if cv2.waitKey(1) & 0xFF == ord('q'):
        #        break

        #cv2.destoryAllWindows()
        self.clisock.close()
        self.thread_stop = True


if __name__ == "__main__":
    sock()
