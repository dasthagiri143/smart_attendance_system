import cv2

print("[INFO] Trying AVFoundation backend...")

# Try with AVFoundation backend (common for MacOS)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# If AVFoundation fails, fallback to default
if not cap.isOpened():
    print("[WARN] AVFoundation failed, trying default VideoCapture...")
    cap = cv2.VideoCapture(0)

print(f"[INFO] CAP_OPENED: {cap.isOpened()}")

if not cap.isOpened():
    print("[FATAL] Cannot open webcam. Check camera permissions in System Preferences > Security & Privacy > Camera.")
    exit()

while True:
    ret, frame = cap.read()
    print(f"[DEBUG] ret: {ret} | frame type: {type(frame)}")

    if not ret:
        print("[ERROR] Failed to grab frame.")
        continue

    cv2.imshow("Test Webcam — Press q to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Quit requested.")
        break

cap.release()
cv2.destroyAllWindows()
