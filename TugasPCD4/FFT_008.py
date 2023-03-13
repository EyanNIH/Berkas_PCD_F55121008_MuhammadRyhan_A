import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
img = cv2.imread('Street.jpg', 0)

# Melakukan FFT pada gambar
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Mencari magnitude spectrum dari hasil FFT
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Menampilkan gambar dan magnitude spectrum
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()