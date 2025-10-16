import numpy as np
import cv2
import imutils
import datetime
import time

# Load the Haar cascade for gun detection
gun_cascade = cv2.CascadeClassifier(
    r"C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\Weapon_Detection_Using_Python_OpenCV\cascade.xml"
)

# Check if the cascade loaded correctly
if gun_cascade.empty():
    print("Error: Could not load cascade file.")
    exit()

# Initialize video capture
camera = cv2.VideoCapture(0)
time.sleep(2)  # Give the camera time to warm up

firstFrame = None
gun_detected = False  # Track detection across frames

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame.")
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the frame with stricter parameters to reduce false positives
    guns = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,       # Slightly higher to reduce sensitivity
        minNeighbors=8,        # More neighbors = higher confidence
        minSize=(100, 100)     # Minimum size of detected object
    )

    if len(guns) > 0:
        gun_detected = True
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Gun detected in frame.")

    # Draw rectangles around detected guns
    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Final detection result
print("\nSession Summary:")
if gun_detected:
    print("Gun was detected during this session.")
else:
    print("No guns were detected during this session.")

camera.release()
cv2.destroyAllWindows()
