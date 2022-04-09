from dataclasses import dataclass
from time import sleep

from pillcontroler import PillController
from motor import Motor


@dataclass
class Time:
    d: str = "Mon"
    h: int = 0
    m: int = 0


class MainRobot:
    def __init__(self):
        self.pc = PillController(tty_str='COM5')

        motor_pin_1 = 32
        AIN_1 = 38
        AIN_2 = 40
        motor_pin_2 = 33
        BIN_1 = 35
        BIN_2 = 37
        LED = 11

        self.motor = Motor(motor_pin_1, motor_pin_2, AIN_1, AIN_2, BIN_1, BIN_2, LED)

        self.current_time = Time()
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.time_speed = 0.001  # ile czasu w sekundach trwa minuta

    def main_loop(self):
        while True:
            for day in self.days:
                self.current_time.d = day
                for hour in range(24):
                    self.current_time.h = hour
                    if self.current_time.h < 10:
                        hour_string = f"0{self.current_time.h}"
                    else:
                        hour_string = f"{self.current_time.h}"

                    for minute in range(60):
                        self.current_time.m = minute

                        self.motor.go()

                        if self.current_time.m < 10:
                            minute_string = f"0{self.current_time.m}"
                        else:
                            minute_string = f"{self.current_time.m}"

                        current_time_string = f"{self.current_time.d} " + hour_string + minute_string

                        if current_time_string in self.pc.rotation.keys():
                            print(self.pc.rotation[current_time_string])

                        self.pc.drop_pills(self.pc.rotation[current_time_string])

                        sleep(self.time_speed)


if __name__ == '__main__':
    mr = MainRobot()
    mr.main_loop()

    # pc = PillController(tty_str='COM5')
    #
    # pc.pill_boxes[5].drop_pill()
    # con = Controller('COM5')
    # print("start")
    # con.setTarget(1, 1500)
