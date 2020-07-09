
#uses trackbar to find the upper and lower hsv values for required colour to be identified
#for image

#color_identifier(np.array([0,158,87]), np.array([17,255,255]) ##for red
#color_identifier(np.array([55,64,64]), np.array([94,255,255])) ##for green
# You can track your custom color which you can replace with the codes of the main file

#  YOU CAN CHANGE THE COLOR VALUE BELOW ACCORDING TO YOUR CLOTH COLOR
#   lower_red = np.array([0, 120, 50])
#   upper_red = np.array([10, 255,255])
#   mask1 = cv2.inRange(hsv, lower_red, upper_red)

#    lower_red = np.array([170, 120, 70])
#    upper_red = np.array([180, 255, 255])
#    mask2 = cv2.inRange(hsv, lower_red, upper_red)



import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
# Initialising the Trackbar
cv2.createTrackbar("LH", "Tracking", 110, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 120, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 50, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 130, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('invisibleclock_demo_image.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    # Comment the lines of frame and res and compare the masking frame to choose your color

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
