import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("apple.jpg", 0)
# sobel
sobelx = np.array([[-2, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobely = np.array([[1, 2, 1], [0, 0, 0], [-1, 0, -1]])
img_sobelx = cv.filter2D(img, -1, sobelx)
img_sobely = cv.filter2D(img, -1, sobely)
sobel = cv.add(img_sobelx, img_sobely)

# robert
robertx = np.array([[1, 0], [0, 1]])
roberty = np.array([[0, 1], [-1, 0]])

img_robertx = cv.filter2D(img, -1, robertx)
img_roberty = cv.filter2D(img, -1, roberty)
robert = cv.add(img_robertx, img_roberty)

# prewitt
prewitx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewity = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
img_prewitx = cv.filter2D(img, -1, prewitx)
img_roberty = cv.filter2D(img, -1, prewity)
prewit = cv.add(img_prewitx, img_roberty)

# out original
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

# out sobel
plt.subplot(2, 2, 2), plt.imshow(sobel, cmap='gray')
plt.title('sobel'), plt.xticks([]), plt.yticks([])

# out robert
plt.subplot(2, 2, 3), plt.imshow(robert, cmap='gray')
plt.title('Robert'), plt.xticks([]), plt.yticks([])

# out prewit
plt.subplot(2, 2, 4), plt.imshow(prewit, cmap='gray')
plt.title('Prewit'), plt.xticks([]), plt.yticks([])
plt.show()


