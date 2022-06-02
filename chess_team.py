import cv2
import numpy as np

image = cv2.imread("player_orange.jpg")
# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define blue color range
light_blue = np.array([110, 50, 50])
dark_blue = np.array([130, 255, 255])

light_orange = np.array([10, 100, 20])
dark_orange = np.array([25, 255, 255])

mask_blue = cv2.inRange(hsv, light_blue, dark_blue)
mask_orange = cv2.inRange(hsv, light_orange, dark_orange)

# Determine if the color exists on the image
if cv2.countNonZero(mask_blue) > 5:
    print('Team Blue is present!')
elif cv2.countNonZero(mask_orange) > 5:
    print('Orange Team is present!')
else:
    print("block is empty")


