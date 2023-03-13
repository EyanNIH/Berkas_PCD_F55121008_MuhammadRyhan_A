import cv2

# Load the two images
img1 = cv2.imread('foto1.jpg')
img1 = cv2.resize(img1, (326, 536))
img2 = cv2.imread('foto2.jpg')
img2 = cv2.resize(img2, (326, 536))

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imshow('Difference Image', thresh)
cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)
cv2.waitKey(0)
