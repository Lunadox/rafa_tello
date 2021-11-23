from djitellopy import Tello

tello = Tello()

tello.connect()
# 연결
tello.takeoff()
# 이륙

tello.move_up(50) # 안전을 위해 50cm업
tello.move_forward(55) # 전진명령(cm)
# tello.move_forward(55)
tello.rotate_clockwise(360) # 시계방향으로 회전(degree)

tello.move_back(55) # 후진명령(cm)
# tello.move_back(55)

tello.land()
# 착륙
pass