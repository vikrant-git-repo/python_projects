import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier(r"C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\Weapon_Detection_Using_Python_OpenCV\cascade.xml")
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = None

while True:

    ret, frame = camera.read()
    
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gun = gun_cascade.detectMultiScale(gray,
                                      1.3, 5,
                                      minSize=(100, 100))
    
    if len(gun) > 0:
        gun_exist = True
        
    for(x, y, w, h) in gun:
        frame = cv2.rectangle(frame,
                             (x,y),
                             (x+w, y+h),
                             (255,0,0), 2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
        
    if firstFrame is None:
        firstFrame = gray
        continue
        
    cv2.imshow("Security feed", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
        
if gun_exist:
    print("Gun detected")
else:
    print("No guns detected")
    
camera.release()
cv2.destroyAllWindows()


