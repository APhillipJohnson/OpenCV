import cv2

def generate():
    face_cascade = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_eye.xml')
    #camera = cv2.VideoCapture(0)
    count = 0;
    #ret, frame = camera.read()


    while (True):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)

            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))

            cv2.imwrite('/home/nemo/opencv-3.0.0/data/at/ckh/%s.pgm' % str(count), f)
            count += 1

        cv2.imshow("camera", frame)
        if cv2.waitKey(30) & 0xff == ord('q'):
            break
        
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    generate()