# coding:utf-8


# 600~2400代表0~180

armNum = {"L1": '0D', "L2": '0E',"L3": '0F', "L4": '18', "L5": '19', "L6": '1A',
          "R1": '0C', "R2": '0B', "R3": '0A', "R4": '07', "R5": '06', "R6": '05'}
fingerNum = {"L1": '1F', "L2": '1E',"L3": '1D', "L4": '1C', "L5": '1B',
            "R1": '00', "R2": '01', "R3": '02', "R4": '03', "R5": '04'}


# 加一个angle必须要在一位小数的约束。0.3度的控制
def angle2pwm(angle):
    pwm = angle * 10 + 600
    return pwm


def angle2cmd_hex(angle):
    return cmd2cmd_hex(angle2pwm(angle))


def number2cmd_hex(number):
    if number < 16:
        return "0"+str(hex(number))[2:3].upper()
    else:
        return str(hex(number))[2:].upper()


def cmd2cmd_hex(number):
    tempstr = str(hex(number)[2:]).upper().zfill(4)  # 用0补齐4位
    low_eight = tempstr[2:]
    high_eight = tempstr[:2]
    return low_eight, high_eight




