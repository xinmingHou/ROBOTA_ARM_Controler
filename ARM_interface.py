# coding:utf-8
from physicial_parament import *
import serial


"""
大臂运动角：0° ~ 180°（2个舵机）  PWM脉宽600~2400us
小臂运动角：0° ~ 180°（2个舵机）  PWM脉宽600~2400us
手腕摆动角：-45° ~ ﹢45°（1个舵机） PWM脉宽600~2400us
手腕翻转角：-90° ~ ﹢90°（1个舵机） PWM脉宽600~2400us
手指运动角：伸直 ~ 弯曲（1个舵机）  PWM脉宽1000~2000us


55 55 08 03 01 E8 03 (舵机ID) --  --
"""


class ARMcontroler:
    def __init__(self, serial_name):
        self.cmd_time = "D007"  # 2000ms
        self.ser = serial.Serial(serial_name, 9600, timeout=2)
        print("check which port was really used >", self.ser.name)
        print("open serial")
        if self.ser.is_open:
            print("serial is open")
        else:
            print("serial not open")
            exit(0)

    def __sendcmd(self, cmdsend):
        print(cmdsend)
        cmdsend = cmdsend.decode("hex")
        self.ser.write(cmdsend)

    # 运行时间默认为1000ms
    def CMD_SERVO_MOVE(self, ID_angle):
        number = len(ID_angle)
        cmd_number = number2cmd_hex(number)
        cmd_length = number2cmd_hex(number*3+5)
        cmd_time = self.cmd_time
        cmdsend = "5555" + cmd_length + "03" + cmd_number + cmd_time
        for ID, angle in ID_angle:
            low_eight, high_eight = angle2cmd_hex(angle)
            cmdsend = cmdsend + ID + low_eight + high_eight
        self.__sendcmd(self.ser, cmdsend)

    # 运行动作组，及次数，0为无数次
    def CMD_ACTION_GROUP_RUN(self, groupID, times):
        cmdsend = "55550506" + number2cmd_hex(groupID)
        low_eight, high_eight = cmd2cmd_hex(times)
        cmdsend = cmdsend + low_eight + high_eight
        self.__sendcmd(self.ser, cmdsend)

    # 停止正在运行的工作组
    def CMD_ACTION_GROUP_STOP(self):
        cmdsend = "55550207"
        self.__sendcmd(self.ser, cmdsend)

    # 归位，或是到中间位置
    def CMD_reset(self, ori=True):
        if ori:
            self.CMD_ACTION_GROUP_RUN(0, 1)
        else:
            self.CMD_ACTION_GROUP_RUN(1, 1)














