import cv2.cv as cv

import time

if __name__ == '__main__':

    cv.NamedWindow("camera",1)
    capture = cv.CaptureFromCAM(0)  

    while True:
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera",img)
        mm = int(time.strftime('%S',time.localtime()))

        if mm == 30:
            filename = "e:\pic\o\%s.jpg" % time.strftime('%Y%m%d%H%M%S',time.localtime())
        #time.sleep(2)
            cv.SaveImage(filename,img)
        if cv.WaitKey(10) == 27:
            break

    del(capture)
    cv.DestroyWindow("camera")
