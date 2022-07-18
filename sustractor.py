import numpy as np
import cv2


#background sustraccion

capp = cv2.VideoCapture('t2.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
fgmask = 't2.mp4'

def run():
    while(1):
        ret, frame = capp.read()
        fgmask = fgbg.apply(frame)
        #cv2.imshow('fgmask', fgmask)
        #cv2.imshow('frame',frame )
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

def fgmask_result():
    run()
    return fgmask