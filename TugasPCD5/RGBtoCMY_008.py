import numpy as np
import cv2

def RGBkeCMY(R, G, B):
    # RGBkeCMY digunakan untuk mengonversi RGB ke CMYK
    # Normalisasi RGB ke [0, 1]
    R = R.astype(float)
    G = G.astype(float)
    B = B.astype(float)

    if np.max(R) > 1.0 or np.max(G) > 1.0 or np.max(B) > 1.0:
        R /= 255.0
        G /= 255.0
        B /= 255.0

    u = 0.5
    b = 1
    tinggi, lebar = R.shape
    C = np.zeros((tinggi, lebar), dtype=np.uint8)
    M = np.zeros((tinggi, lebar), dtype=np.uint8)
    Y = np.zeros((tinggi, lebar), dtype=np.uint8)
    K = np.zeros((tinggi, lebar), dtype=np.uint8)
    for m in range(tinggi):
        for n in range(lebar):
            Kb = min([(1 - R[m, n]), (1 - G[m, n]), (1 - B[m, n])])
            if Kb == 1:
                C[m, n] = 0
                M[m, n] = 0
                Y[m, n] = 0
            else:
                C[m, n] = (1.0 - R[m, n] - u * Kb) * 255
                M[m, n] = (1.0 - G[m, n] - u * Kb) * 255
                Y[m, n] = (1.0 - B[m, n] - u * Kb) * 255
                K[m, n] = b * Kb * 255

    return C, M, Y, K

# Load image
img = cv2.imread('Eren.png')

# Split channels
B, G, R = cv2.split(img)

# Convert RGB to CMYK
C, M, Y, K = RGBkeCMY(R, G, B)

# Merge channels
CMYK = cv2.merge((C, M, Y, K))

# Display result
cv2.imshow('RGB image', img)
cv2.imshow('CMYK image', CMYK)
cv2.waitKey(0)
cv2.destroyAllWindows()