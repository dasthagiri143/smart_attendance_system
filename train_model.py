import face_recognition
import os
import cv2
import pickle

dataset_dir = "dataset"
known_encodings = []
known_names = []

for name in os.listdir(dataset_dir):
    person_dir = os.path.join(dataset_dir, name)
    for filename in os.listdir(person_dir):
        image_path = os.path.join(person_dir, filename)
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(name)

data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Model trained and saved as encodings.pkl")
