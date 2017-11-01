import cv2

def detect():
    face_cascade = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            
        cv2.imshow('camera', frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()
