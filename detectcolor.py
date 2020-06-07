import cv2
import numpy as np



cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")
cv2.createTrackbar("B", "frame", 0, 255, nothing)
cv2.createTrackbar("G", "frame", 0, 255, nothing)
cv2.createTrackbar("R", "frame", 0, 255, nothing)



cap.set(3, 480)
cap.set(4, 320)

_, frame = cap.read()
rows, cols, _ = frame.shape

#x_medium = int(cols / 2)
#center = int(cols / 2)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    b = cv2.getTrackbarPos("B", "frame")
    g = cv2.getTrackbarPos("G", "frame")
    r = cv2.getTrackbarPos("R", "frame")

    
    low_red = np.array([153,255,255])
    high_red = np.array([0,255,255])

    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    _, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0, 255, 0), 2)
    #   x_medium = int((x + x + w) / 2)
        break
    
    #cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    red_mask=cv2.cvtColor(red_mask,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", frame)
    cv2.imshow("gray", red_mask)
    
    key = cv2.waitKey(1)
    
    if key == 27:
        break

    
cap.release()
cv2.destroyAllWindows()
