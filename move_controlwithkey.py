from djitellopy import Tello, tello
import cv2 as cv

tello = Tello()

tello.connect()
# 연결
img = cv.imread("./tello_drone.png")
cv.imshow('tello image',img)

# 여기에 연결이 됐는지 확인하는 예외처리가 필요함

# 움직임 제어 키보드로 하는
while True:
    key = cv.waitKey(2)
    if key == ord('t'):
        tello.takeoff()
        # 이륙
    elif key == 32:
        tello.move_up(50)
        # 위로(cm) 스페이스바
    elif key == 82:
        tello.move_forward(50)
        # 앞으로(cm) 방향키 앞
    elif key == 84:  
        tello.move_back(50)
        # 뒤로(cm) 방향키 뒤
    elif key == 83:
        tello.rotate_clockwise(360)
        # 회전(degree) 방향키 오른쪽
    # if key >-1:
    #     print(key)
    elif key == ord('q'):
        break # 반복문 탈출

tello.land() # 착륙

# 

pass

#  # 안전을 위해 50cm업

# # 시계방향으로 회전(degree)


