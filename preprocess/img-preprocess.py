import cv2
import numpy as np

kernel = np.ones((3,3),np.uint8)

img = cv2.imread("dataset/gol.jpg")

#converte p/ escala cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur image with various low pass filters (median blur)
median = cv2.medianBlur(gray,7)

# Apply adaptive thresholding to segment the characters
thresh = cv2.adaptiveThreshold(median, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11, 2)

# Apply 
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
invert = cv2.bitwise_not(closing)
cv2.imshow("thresh", thresh)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows






# roi=cv2.selectROI(invert)
# roi_cropped=invert[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

# cv2.imshow("ROI",roi_cropped)