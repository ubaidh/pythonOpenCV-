import cv2
cap=cv2.VideoCapture(0)
while True:
    ret , frame =cap.read()
    cv2.namedWindow("frame")
    frame=cv2.resize(frame,(1600,800))
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()