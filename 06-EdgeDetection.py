import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)

while(True):
    rec, frame = cap.read(1)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame, (7, 7), 0)
    
    # frame = cv.Canny(frame, 100, 200)
    frame = cv.Sobel(src=frame, ddepth=cv.CV_64F, dx=0, dy=1, ksize=3)

    cv.imshow('frame', frame)
    keyexit = cv.waitKey(5) & 0xff
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()