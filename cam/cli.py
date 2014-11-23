#!/usr/bin/env python
# coding=utf-8

#  ------------------------------------
#  Create date : 2014-11-23 20:02
#  Author : Wangzhaojiang
#  Email : wangzhaojiang2013@gmail.com
#  ------------------------------------
import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)

    return buf

def sock():
    HOST = '127.0.0.1'
    PORT = 10000
    ADDR = (HOST, PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ADDR)

    while True:
        s.send('yes')
        length = recvall(s, 16)
        stringData = recvall(s, int(length))
        data = numpy.fromstring(stringData, dtype = 'uint8')
        decimg = cv2.imdecode(data, 1)
        cv2.imshow('client', decimg)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            s.send('no')
            break

    
    cv2.destroyAllWindows()
    s.close()

if __name__ == '__main__':
    sock()
