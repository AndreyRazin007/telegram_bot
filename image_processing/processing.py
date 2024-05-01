import cv2
import dlib
from imutils import face_utils
import matplotlib.pyplot as pyplot

font = cv2.FONT_HERSHEY_SIMPLEX

cascade_path = "./models/haarcascade_frontalface_default.xml"
eye_path = "./models/haarcascade_eye.xml"
smile_path = "./models/haarcascade_smile.xml"

face_cascade = cv2.CascadeClassifier(cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_path)
smile_cascade = cv2.CascadeClassifier(smile_path)

gray = cv2.imread("./Screenshot_1.png")

pyplot.figure(figsize=(12, 8))
pyplot.imshow(gray, cmap="gray")
pyplot.show()

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 3)

pyplot.figure(figsize=(12, 8))
pyplot.imshow(gray, cmap="gray")
pyplot.show()
