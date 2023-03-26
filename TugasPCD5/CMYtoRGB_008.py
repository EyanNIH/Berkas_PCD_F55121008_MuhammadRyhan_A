import numpy as np
import cv2


def CMYkeRGB(C, M, Y, K):
    # CMYkeRGB digunakan untuk mengonversi CMYK ke RGB
    # Berdasarkan Pratt(2001)
    # Dasar: b = 1 dan u = 0,5

    # Normalisasi CMY ke [0, 1]
    C = C.astype(float)
    M = M.astype(float)
    Y = Y.astype(float)
    K = K.astype(float)

    if np.max(C) > 1.0 or np.max(M) > 1.0 or np.max(Y) > 1.0 or np.max(K) > 1.0:
        C /= 255.0
        M /= 255.0
        Y /= 255.0
        K /= 255.0

    u = 0.5
    b = 1
    tinggi, lebar = C.shape
    R = np.zeros((tinggi, lebar), dtype=np.uint8)
    G = np.zeros((tinggi, lebar), dtype=np.uint8)
    B = np.zeros((tinggi, lebar), dtype=np.uint8)

    for m in range(tinggi):
        for n in range(lebar):
            Kb = K[m, n] / b
            if Kb == 1:
                R[m, n] = 0
                G[m, n] = 0
                B[m, n] = 0
            else:
                R[m, n] = (1.0 - C[m, n] - u * Kb) * 255
                G[m, n] = (1.0 - M[m, n] - u * Kb) * 255
                B[m, n] = (1.0 - Y[m, n] - u * Kb) * 255

    return R, G, B


img = cv2.imread('Eren.png')
C = 1.0 - img[:, :, 0] / 255.0
M = 1.0 - img[:, :, 1] / 255.0
Y = 1.0 - img[:, :, 2] / 255.0
K = np.min(np.stack([C, M, Y]), axis=0)
C = (C - K) / (1.0 - K)
M = (M - K) / (1.0 - K)
Y = (Y - K) / (1.0 - K)

R, G, B = CMYkeRGB(C, M, Y, K)

cv2.imshow('RGB', cv2.merge([B, G, R]))
cv2.waitKey(0)
cv2.destroyAllWindows()
