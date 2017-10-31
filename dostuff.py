import cv2

fp = '/home/nemo/Pictures/base_picture.jpg'

def detect(fp):
    face_cascade = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(fp)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray colorspace req. for detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
       img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.namedWindow('It is me!!')
    cv2.imshow('I have been detected!!', img)
    cv2.imwrite('/home/nemo/Pictures/base.jpg', img)
    cv2.waitKey(0)
detect(fp)