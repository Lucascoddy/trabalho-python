import cv2
img = cv2.imread("lucas_color.jpg", 1)
canny = cv2.Canny(img, 255, 100)
cv2.imshow('lucas', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
