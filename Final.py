import threading
import cv2
import os

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def send_whatsapp():
    os.system("python whats.py")


def send_mail():
    os.system("python send_mail.py")


def face_detector(img, size=0.5):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi



# Open Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
adarsh_model = cv2.face_LBPHFaceRecognizer.create()
aditya_model = cv2.face_LBPHFaceRecognizer.create()
adarsh_model.read("adarsh.yml")
aditya_model.read("aditya.yml")
count = 1
count2 = 1
while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        results = adarsh_model.predict(face)
        results2 = aditya_model.predict(face)
        name = ""
        if results[1] > results2[1]:
            name = "Hey Aditya"
        else:
            name = "Hey Adarsh"


        if name == "Hey Adarsh":
            if results[1] < 500:
                confidence = int(100 * (1 - (results[1]) / 400))
                display_string = str(confidence) + '% Confident it is User'
        else:
            if results2[1] < 500:
                confidence = int(100 * (1 - (results[1]) / 400))
                display_string = str(confidence) + '% Confident it is User'


        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)

        if confidence >= 90:
            cv2.putText(image, name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', image)
            if name == "Hey Adarsh":
                count += 1
                if count == 5:
                    t2 = threading.Thread(target=send_mail)
                    t2.start()
                    t1 = threading.Thread(target=send_whatsapp)
                    t1.start()
                    t1.join()
            else:
                count2 += 1
                if count2 == 5:
                    os.system("terraform apply -auto-approve")

        else:
            cv2.putText(image, "I dont know, who r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)

    except:
        cv2.putText(image, "No Face Found", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face Recognition', image)
        pass

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()