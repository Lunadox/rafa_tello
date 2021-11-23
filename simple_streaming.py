from djitellopy import Tello

tello = Tello()

tello.connect()

import cv2 as cv
tello.streamon()

key = cv.waitKey()
# tello video
while True:
    frame_read=tello.get_frame_read()
    cv.imshow(' ',frame_read.frame)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
tello.streamoff()
pass