import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(detectionCon= 0.5, maxHands=1)

while(True):
    rec, frame = cap.read()
    hand, img = detector.findHands(frame)
    cv.imshow('frame', frame)
    keyexit = cv.waitKey(5) & 0xff
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()