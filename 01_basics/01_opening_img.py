import cv2
img = cv2.imread("640.jpg")
cv2.imshow("img",img)
if cv2.waitKey(0) & 0xff==ord('q'):
    cv2.destroyAllWindows()