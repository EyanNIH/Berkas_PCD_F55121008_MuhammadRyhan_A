import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('desa.jpg', 0)

# Apply histogram equalization to the image
eq_img = cv2.equalizeHist(img)

# Calculate the histogram of the equalized image
eq_hist = cv2.calcHist([eq_img], [0], None, [256], [0, 256])

# Display the original and equalized images side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[1].imshow(eq_img, cmap='gray')
axs[1].set_title('Equalized Image')
plt.show()

# Plot the histograms of the original and equalized images
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].plot(cv2.calcHist([img], [0], None, [256], [0, 256]))
axs[0].set_title('Original Histogram')
axs[1].plot(eq_hist)
axs[1].set_title('Equalized Histogram')
plt.show()
