import cv2
import os

import os

name = os.environ.get("NEW_NAME") or input("Enter name: ")
dataset_path = "dataset/" + name

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    cv2.imshow("Capturing — Press q to quit", frame)
    cv2.imwrite(f"{dataset_path}/{name}_{count}.jpg", frame)
    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 20:
        break

cap.release()
cv2.destroyAllWindows()
