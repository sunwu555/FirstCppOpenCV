import cv2
import numpy as np
import matplotlib as plt

# read an image
img = cv2.imread('hand.jpg')

# conver the color to gray scale by using opencv
gray_hand = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# dispay image to console
cv2.imshow('gray_color_hand', gray_hand)
cv2.waitKey(0)
cv2.destroyAllWindows()