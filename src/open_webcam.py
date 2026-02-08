import cv2

cap = cv2.VideoCapture(0)

def camera():
    if not cap.isOpened():
        print("Failed to open camera")
        exit()
    while True:
        ret,frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        cv2.imshow("Camera",frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    
    cap.release()