import cv2

def detect():
    '''
    This initializes the webcam, and creates a box around the face. 
    It can take a little bit of time to redefine box after quick movements 
    of face out of frame and back in.
    '''
    face = cv2.CascadeClassifier('/home/nemo/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)

            
        cv2.imshow('camera', frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()
