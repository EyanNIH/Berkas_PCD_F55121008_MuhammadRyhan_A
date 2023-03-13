import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('street.jpg', 0)

# Fourier Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Inverse Fourier Transform
ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(ishift)
img_back = np.abs(img_back)

# Unsharp Masking
unsharp_img = cv2.GaussianBlur(img, (0,0), 5)
unsharp_img = cv2.addWeighted(img, 1.5, unsharp_img, -0.5, 0)

# Laplacian Domain Frekuensi
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplacian_img = cv2.filter2D(img, -1, kernel)

# Selective Filtering
gaussian = cv2.GaussianBlur(img, (15,15), 5)
diff = cv2.absdiff(img, gaussian)
selective_img = cv2.addWeighted(img, 1.5, diff, -0.5, 0)

# Display the results
titles = ['Original Image', 'Unsharp Masking', 'Laplacian Domain Frekuensi', 'Selective Filtering']
images = [img, unsharp_img, laplacian_img, selective_img]
for i in range(4):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()