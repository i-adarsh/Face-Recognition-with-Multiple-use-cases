import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# Get the training data we previously made
data_path = '/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Computer_Vision/Face_Recognition/faces/user/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

data_path2 = '/Users/adarshkumar/Documents/PycharmProjects/PythonProject/Computer_Vision/Face_Recognition/faces/user1/'
onlyfiles2 = [f for f in listdir(data_path2) if isfile(join(data_path2, f))]

# Create arrays for training data and labels
Training_Data, Labels = [], []
Training_Data2, Labels2 = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)


for i, files2 in enumerate(onlyfiles2):
    image_path2 = data_path2 + onlyfiles2[i]
    images2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    Training_Data2.append(np.asarray(images2, dtype=np.uint8))
    Labels2.append(i)


# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)
Labels2 = np.asarray(Labels2, dtype=np.int32)

# Initialize facial recognizer
# model = cv2.face.createLBPHFaceRecognizer()
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()
# pip install opencv-contrib-python
# model = cv2.createLBPHFaceRecognizer()

adarsh_model  = cv2.face_LBPHFaceRecognizer.create()
aditya_model = cv2.face_LBPHFaceRecognizer.create()


# Let's train our model
adarsh_model.train(np.asarray(Training_Data), np.asarray(Labels))
aditya_model.train(np.asarray(Training_Data2), np.asarray(Labels2))

adarsh_model.save("adarsh.yml")
aditya_model.save("aditya.yml")
print("Model trained sucessefully")



