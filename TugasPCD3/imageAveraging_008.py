import cv2
import numpy as np

# Load the images
img1 = cv2.imread('foto1.jpg')
img1 = cv2.resize(img1, (326, 536))
img2 = cv2.imread('foto2.jpg')
img2 = cv2.resize(img2, (326, 536))

# Average the images
avg_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the averaged image
cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
