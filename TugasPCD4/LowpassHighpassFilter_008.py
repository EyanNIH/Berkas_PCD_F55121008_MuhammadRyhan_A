import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
img = cv2.imread('street.jpg', 0)

# Compute the Fourier Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Compute the magnitude spectrum
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# Define the filter functions
def ideal_lowpass_filter(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), dtype=np.uint8)
    mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 1
    return mask

def butterworth_lowpass_filter(shape, cutoff, order):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    u, v = np.meshgrid(np.arange(cols) - ccol, np.arange(rows) - crow)
    d = np.sqrt(u**2 + v**2)
    filter = 1 / (1 + (d / cutoff)**(2 * order))
    return filter

def gaussian_lowpass_filter(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    u, v = np.meshgrid(np.arange(cols) - ccol, np.arange(rows) - crow)
    d = np.sqrt(u**2 + v**2)
    filter = np.exp(-(d**2) / (2 * cutoff**2))
    return filter

# Highpass
def ideal_highpass_filter(image, d0):
    rows, cols = image.shape
    center_row, center_col = rows//2, cols//2
    mask = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if np.sqrt((i - center_row)**2 + (j - center_col)**2) > d0:
                mask[i, j] = 1
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)
    filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(mask * fft_shifted)))
    return filtered_image

def gaussian_highpass_filter(image, d0):
    rows, cols = image.shape
    center_row, center_col = rows//2, cols//2
    mask = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            mask[i, j] = 1 - np.exp(-((i - center_row)**2 + (j - center_col)**2) / (2 * d0**2))
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)
    filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(mask * fft_shifted)))
    return filtered_image

def butterworth_highpass_filter(image, d0, n):
    rows, cols = image.shape
    center_row, center_col = rows//2, cols//2
    mask = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - center_row)**2 + (j - center_col)**2)
            mask[i, j] = 1 - 1 / (1 + (distance / d0)**(2 * n))
    fft_image = np.fft.fft2(image)
    fft_shifted = np.fft.fftshift(fft_image)
    filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(mask * fft_shifted)))
    return filtered_image

# Apply the filters
d0 = 50
n = 2
filtered_image1 = ideal_highpass_filter(img, d0)
filtered_image2 = gaussian_highpass_filter(img, d0)
filtered_image3 = butterworth_highpass_filter(img, d0, n)

ideal_filter = ideal_lowpass_filter(img.shape, 50)
butterworth_filter = butterworth_lowpass_filter(img.shape, 50, 2)
gaussian_filter = gaussian_lowpass_filter(img.shape, 50)

f_ideal = fshift * ideal_filter
f_butterworth = fshift * butterworth_filter
f_gaussian = fshift * gaussian_filter

# Compute the inverse Fourier Transform
img_ideal = np.abs(np.fft.ifft2(np.fft.ifftshift(f_ideal)))
img_butterworth = np.abs(np.fft.ifft2(np.fft.ifftshift(f_butterworth)))
img_gaussian = np.abs(np.fft.ifft2(np.fft.ifftshift(f_gaussian)))

# Display the results
plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(img_ideal, cmap='gray')
plt.title('Ideal Lowpass Filter'), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(img_gaussian, cmap='gray')
plt.title('Gaussian Lowpass Filter'), plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(img_butterworth, cmap='gray')
plt.title('Butterworth Lowpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()

# Show results
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(2, 2, 2)
plt.imshow(filtered_image1, cmap='gray')
plt.title('Ideal highpass filter')

plt.subplot(2, 2, 3)
plt.imshow(filtered_image2, cmap='gray')
plt.title('Gaussian highpass filter')

plt.subplot(2, 2, 4)
plt.imshow(filtered_image3, cmap='gray')
plt.title('Butterworth highpass filter')

plt.show()

