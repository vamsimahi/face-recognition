import cv2
import os

video=cv2.VideoCapture(0)

fd = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count=0

name = str(input("Enter your name")).lower()

path='Images/' +name

isExist = os.path.exists(path)

if isExist:
    print("name aleay taken")
    name=str(input("Enter name again"))
else:
    os.makedirs(path)


while True:
    ret,frame = video.read()
    faces=fd.detectMultiScale(frame,1.3,5)
    for x,y,w,h in faces:
        count=count+1
        names=' .Images/'+'name'+'/' + str(count) + '.jpg'
        print('creating images' +names)
        cv2.imwrite(names,frame[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 3)
    cv2.imshow("windowFrame",frame)
    cv2.waitKey(1)
    if count>1:
        break
video.release()
cv2.destroyAllWindows()
