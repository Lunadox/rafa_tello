from djitellopy import Tello

tello = Tello()

tello.connect()

import cv2 as cv
tello.streamon()
while True:
    key = cv.waitKey()
    frame_read=tello.get_frame_read()
    cv.imshow(' ',frame_read.frame)
# tello.takeoff()

# tello.land()
    cv.waitKey(10)
    if key==ord('q'):
        tello.streamoff()
        break

pass