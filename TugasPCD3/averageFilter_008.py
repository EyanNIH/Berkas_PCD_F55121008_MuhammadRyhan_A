import cv2
import numpy as np

# Load the image
img = cv2.imread('kota.jpg')

# Define the kernel size for the filter (in this case, 5x5)
kernel_size = (5, 5)

# Create the kernel for the filter
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

# Apply the filter to the image
filtered_img = cv2.filter2D(img, -1, kernel)

# Display the original and filtered images side by side
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
