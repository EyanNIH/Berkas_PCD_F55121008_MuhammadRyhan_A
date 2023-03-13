import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('kota.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram of the grayscale image
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(hist)

# Show the histogram
plt.show()
