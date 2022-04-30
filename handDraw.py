import cv2
import numpy as np


#user input                                                                     
imgChoice = input('Input image title:')

#import image and convert
img = cv2.imread(imgChoice)
cv2.imshow("Original",img)
cv2.waitKey(0)

#make black and white to detect edges, blur image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 3) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
cv2.imshow("Edges",edges)
cv2.waitKey(0)

#reimpose colors and edges
color = cv2.bilateralFilter(img, 12, 250, 250) 
final = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Final", final)
cv2.waitKey(0)

cv2.destroyAllWindows() 
