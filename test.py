#coding:utf-8
from ARM_interface import *
import time

serial_name = "/dev/tty.wchusbserial1450"

movement = ARMcontroler(serial_name)

ID_angle = ((armNum["L1"], 70), (armNum['L2'], 90), (armNum['L3'], 50))

movement.CMD_SERVO_MOVE(ID_angle)

time.sleep(2)

movement.CMD_ACTION_GROUP_RUN(1, 1)

time.sleep(6)

movement.CMD_ACTION_GROUP_STOP()

time.sleep(1)

movement.CMD_reset(True)

time.sleep(1)

movement.CMD_reset(False)

time.sleep(1)

movement.CMD_ACTION_GROUP_RUN(0, 1)

time.sleep(2)






