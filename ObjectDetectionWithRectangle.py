import cv2 
import numpy as np

def saveResultImage(img, contours, minarea, maxarea, num):
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if w >= minarea and w < maxarea:
            if h >= minarea and h < maxarea:
                (x,y,w,h) = cv2.boundingRect(contour)
                crop_img=img[y:y+h,x:x+w]
                num = num + 1
                imgname=str(num)
                imgpath="Result/"+imgname+".jpg"
                cv2.imwrite(imgpath,crop_img)
                print(str(num)+"--"+imgpath+"--"+str(w)+" "+str(h))
                print("-------------------")

def detectobject(fram, cascadeclasifier):
    gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
    objs = cascadeclasifier.detectMultiScale(gray, 1.25, 4)
    return objs

def drawrectangle(img, contours, minarea, maxarea):
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if w >= minarea and w < maxarea:
            if h >= minarea and h < maxarea:
                img=cv2.putText(img,str(x) + "," + str(y),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),1)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
                if x >= 30 and x < 392:
                    if (y+h) >= 250 and (y+h) < 320:
                        img=cv2.putText(img,"x=" + str(x) + ",y=" + str(x),
                                        (x,y+h),cv2.FONT_HERSHEY_COMPLEX,
                                        0.5,(255,0,255),1)
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
                        objs = detectobject(img, cascadeclasifier)
                        for (x,y,w,h) in objs:
                            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

def findDiff(fram1, fram2):
    diff = cv2.absdiff(fram1, fram2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours

def transparentarea(image):
    pts=np.array([(200,250),(30,320),(370,320),(392,250)],np.int32)
    imgcop=img.copy()
    cv2.fillPoly(imgcop,[pts],(50,0,0,))
    cv2.addWeighted(imgcop,0.5,img,0.5,0,img)
    cv2.polylines(image,[pts],True,(0,255,0))

cap = cv2.VideoCapture('video2.mp4')
#cap = cv2.VideoCapture(0);
#url = 'https://192.168.43.1:8080/video'
#cap = cv2.VideoCapture(url)
cascadeclasifier = cv2.CascadeClassifier('TrainedHaarCascadeCar.xml')

ret, fram1 = cap.read()
ret, fram2 = cap.read()
minarea = 10
maxarea = 50

while cap.isOpened():

    contours = findDiff(fram1, fram2)
    
    ########   save input   ########
    # saveResultImage(fram1,contours,minarea,maxarea,num)
    ################################
    
    ######## draw rectangle ########
    drawrectangle(fram1, contours, minarea, maxarea)
    ################################
    
    #cv2.drawContours(fram1, contours,-1,(0,255,0),1)
    
    img=cv2.resize(fram1,None,fx=1,fy=1,interpolation=cv2.INTER_CUBIC)
    
    #transparentarea(img)
    
    cv2.imshow("feed", img)
    fram1 = fram2
    ret, fram2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()