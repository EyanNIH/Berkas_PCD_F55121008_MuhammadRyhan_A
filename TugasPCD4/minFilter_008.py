import cv2
import numpy as np

# Membaca citra
img = cv2.imread('Street.jpg')

# Ukuran kernel
ksize = 5

# Min filter
kernel = np.ones((ksize, ksize), np.uint8)
min_filtered = cv2.erode(img, kernel)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Min Filtered Image', min_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()