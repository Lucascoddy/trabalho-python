import cv2
img = cv2.imread("lucas_color.jpg", 1)
stylization = cv2.stylization(img)
cv2.imwrite("lucas efef.png", stylization)
cv2.imshow('lucas', stylization)
cv2.waitKey(0)
cv2.destroyAllWindows()
