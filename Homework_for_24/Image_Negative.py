import cv2
img = cv2.imread("fruits.jpg")
img2 = 255 - img
cv2.imshow("input image : ", img)
cv2.imshow("image negative : ", img2)

cv2.waitKey(100000)
cv2.destroyAllWindows()
