#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr import *

# Brain should be defined by default
brain=Brain()

drivetrain = Drivetrain("drivetrain", 0)
pen = Pen("pen", 8)
pen.set_pen_width(THIN)
left_bumper = Bumper("leftBumper", 2)
right_bumper = Bumper("rightBumper", 3)
front_eye = EyeSensor("frontEye", 4)
down_eye = EyeSensor("downEye", 5)
front_distance = Distance("frontdistance", 6)
distance = front_distance
magnet = Electromagnet("magnet", 7)
location = Location("location", 9)

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Add project code in "main"
from vexcode_vr import *

def forward(d):
    drivetrain.drive_for(FORWARD, d, MM)

def turnright(a):
    drivetrain.turn_for(RIGHT, a, DEGREES)

def turnleft(a):
    drivetrain.turn_for(LEFT, a, DEGREES)

def turn180():          # 왔던 길을 되돌아 오기 위해 180도 회전이 필요
    drivetrain.turn_for(RIGHT, 180, DEGREES)    

def main():             # 갔던길을 그대로 되돌아 오는 코드
    my_list = []        #이동 순서 저잘
    my_dist = []        #이동 거리 저장
    my_ang = []         #회전 각도 저장
    distC = 0
    angC = 0

    my_list.append("180")

    drivetrain.drive_for(FORWARD, 200, MM)
    my_list.append("forward")
    my_dist.append(200)

    drivetrain.turn_for(RIGHT, 40, DEGREES)
    my_list.append("left")
    my_ang.append(40)

    drivetrain.drive_for(FORWARD, 200, MM)
    my_list.append("forward")
    my_dist.append(200)

    my_list.append("180")

    print(my_list)

    r_my_dist = my_dist[::-1]       # [::-1]은 리스트 내용을 뒤집음
    r_my_ang = my_ang[::-1]

    for i in my_list[::-1]:         # 이동 기록을 역순으로 실행
        if(i=="180"):
            turn180()
        if(i=="forward"):
            forward(r_my_dist[distC])
            distC +=1
        if i == "left":
            turnleft(r_my_ang[angC])
            angC += 1

# VR threads — Do not delete
vr_thread(main)
