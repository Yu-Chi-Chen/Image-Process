# import the necessary packages
import numpy as np
import cv2

# first, let's draw a rectangle
rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# secondly, let's draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# A bitwise 'AND' is only True when both rectangle and circlehave
# a value that is 'ON.' Simply put, the bitwise AND function
# examines every pixel in rectangle and circle. If both pixels
# have a value greater than zero, that pixel is turned 'ON' (i.e
# set to 255 in the output image). If both pixels are not greater
# than zero, then the output pixel is left 'OFF' with a value of 0.
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)


# A bitwise 'OR' examines every pixel in rectangle and circle. If
# EITHER pixel in rectangle or circle is greater than zero, then
# the output pixel has a value of 255, otherwise it is 0.
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXOr = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXOr)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("Not", bitwiseNot)
cv2.waitKey(0)
