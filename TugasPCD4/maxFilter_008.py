import cv2
import numpy as np

# Membaca citra
img = cv2.imread('Street.jpg')

# Ukuran kernel
ksize = 5

# Max filter
kernel = np.ones((ksize, ksize), np.uint8)
max_filtered = cv2.dilate(img, kernel)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Max Filtered Image', max_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()