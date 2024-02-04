import cv2

cap = cv2.VideoCapture(0)

while(True):
    rec, frame = cap.read(1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv.GaussianBlur(frame, (3, 3), 0)
    
    frame = cv2.Canny(frame, 50, 50)
    # frame = cv.Sobel(src=frame, ddepth=cv.CV_64F, dx=1, dy=1, ksize=3)

    cv2.imshow('frame', frame)
    keyexit = cv2.waitKey(5) & 0xff
    if keyexit == 27:
        break

cv2.destroyAllWindows()
cap.release()