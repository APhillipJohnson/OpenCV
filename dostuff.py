import cv2
#sets pretaken image to be viewed as variable.
base_pic = '/home/nemo/Pictures/base_picture.jpg'

def detect(base_pic):
    face_cascade = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(base_pic)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray colorspace req. for detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
       img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.namedWindow('It is me!!')
    cv2.imshow('I have been detected!!', img)
    cv2.imwrite('/home/nemo/Pictures/base.jpg', img)
    cv2.waitKey(0)
detect(base_pic)
