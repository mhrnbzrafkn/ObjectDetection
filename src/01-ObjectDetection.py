import cv2

cap = cv2.VideoCapture('../data/videos/video1.avi')
# cap = cv2.VideoCapture(0)


ret, fram1 = cap.read()
ret, fram2 = cap.read()


height = fram1.shape[0]
width = fram1.shape[1]
sc = width/height
w = 500

while cap.isOpened():
    fram1 = cv2.resize(fram1, (int(w*sc), w))
    fram2 = cv2.resize(fram2, (int(w*sc), w))
    
    diff = cv2.absdiff(fram1, fram2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(fram1, contours,-1,(0,255,0),2)

    cv2.imshow("feed", fram1)
    fram1 = fram2
    ret, fram2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()