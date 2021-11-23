from djitellopy import Tello
import cv2
class con_ste:
    def con(self):
        key = cv2.waitKey()
        if key == ord('t'):
            self.takeoff()
        # 이륙
        elif key == 32:
            self.move_up(50)
        # 위로(cm) 스페이스바
        elif key == 82:
            self.move_forward(50)
        # 앞으로(cm) 방향키 앞
        elif key == 84:  
            self.move_back(50)
        # 뒤로(cm) 방향키 뒤
        elif key == 83:
            self.rotate_clockwise(360)
        elif key == ord('l'):
            self.land()

    def ste(self):
        self.streamon()
        while True:
            key = cv2.waitKey()
            frame_read=self.get_frame_read()
            cv2.imshow(' ',frame_read.frame)
            cv2.waitKey(10)
            if key == ord('q'):
                cv2.destroyAllWindows()
                break
        tello.streamoff()
tello = Tello()

tello.connect()

while True:
    # con_ste.ste(tello)
    con_ste.con(tello)

