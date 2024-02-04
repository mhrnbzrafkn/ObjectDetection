import cv2

cap = cv2.VideoCapture('../data/Videos/video3.mp4')
#cap = cv2.VideoCapture(0);


ret, fram1 = cap.read()
ret, fram2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(fram1, fram2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(fram1,contours,-1,(0,255,100),2)

    #height = fram1.shape[0]
    #width = fram1.shape[1]
    #img=cv2.resize(fram1,(width, height))
    img=cv2.resize(fram1,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_CUBIC)
    cv2.imshow("feed", img)
    fram1 = fram2
    ret, fram2 = cap.read()

    if cv2.waitKey(40) == 27:
        break


cv2.destroyAllWindows()
cap.release()
