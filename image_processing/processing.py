import cv2
import matplotlib.pyplot as pyplot

font = cv2.FONT_HERSHEY_SIMPLEX

cascade_path = "./models/haarcascade_frontalface_default.xml"
eye_path = "./models/haarcascade_eye.xml"
smile_path = "./models/haarcascade_smile.xml"

face_cascade = cv2.CascadeClassifier(cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_path)
smile_cascade = cv2.CascadeClassifier(smile_path)

# gray = cv2.imread("./media/themes/emotions_and_expressions/image_1.png")

# pyplot.figure(figsize=(12, 8))
# pyplot.imshow(gray, cmap="gray")
# pyplot.show()

# faces = face_cascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors=5,
#     flags=cv2.CASCADE_SCALE_IMAGE
# )

# for (x, y, w, h) in faces:
#     cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 3)

# pyplot.figure(figsize=(12, 8))
# pyplot.imshow(gray, cmap="gray")
# pyplot.show()

import cv2

import cv2
import matplotlib.pyplot as pyplot

image_1 = cv2.imread("D:\\Programing\\Python\\telegram_bot\\face.jpg")
image_2 = cv2.imread("D:\\Programing\\Python\\telegram_bot\\swap_face.jpg")

result_1 = image_1.copy()
result_2 = image_2.copy()

gray_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
gray_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

faces_1 = face_cascade.detectMultiScale(gray_1, scaleFactor=1.1, minNeighbors=5,
                                        flags=cv2.CASCADE_SCALE_IMAGE, minSize=[0, 1])

faces_2 = face_cascade.detectMultiScale(gray_2, scaleFactor=1.1, minNeighbors=5,
                                        flags=cv2.CASCADE_SCALE_IMAGE, minSize=[0, 1])

if len(faces_1) > 0 and len(faces_2) > 0:
    (x1, y1, w1, h1) = faces_1[0]
    (x2, y2, w2, h2) = faces_2[0]

    face_1 = result_1[y1:y1+h1, x1:x1+w1]
    face_2 = result_2[y2:y2+h2, x2:x2+w2]

    resized_face1 = cv2.resize(face_1, (w2, h2))

    result_2[y2:y2+h2, x2:x2+w2] = resized_face1

    cv2.imshow("Original Image 1", image_1)
    cv2.imshow("Original Image 2", image_2)
    cv2.imshow("Face Replaced Image", result_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Не удалось обнаружить лица на обоих изображениях.")
