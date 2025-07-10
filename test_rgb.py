import cv2
import face_recognition

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    print(f"[DEBUG] BGR: ret={ret}, type={type(frame)}, shape={getattr(frame, 'shape', None)}, dtype={getattr(frame, 'dtype', None)}")

    if not ret or frame is None:
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print(f"[DEBUG] RGB: dtype={rgb_frame.dtype}, shape={rgb_frame.shape}")

    # Try calling face_locations on dummy cropped frame to confirm it works
    try:
        face_locations = face_recognition.face_locations(rgb_frame)
        print(f"[DEBUG] face_locations: {face_locations}")
    except Exception as e:
        print(f"[ERROR] face_recognition failed: {e}")

    cv2.imshow("RGB Test - Press 'q' to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
