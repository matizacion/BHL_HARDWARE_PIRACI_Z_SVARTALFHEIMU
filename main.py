from dataclasses import dataclass
from time import sleep

from pillcontroler import PillController
from motor import Motor

from send_data import comunication_module


@dataclass
class Time:
    d: str = "Mon"
    h: int = 0
    m: int = 0


class MainRobot:
    def __init__(self):
        self.pc = PillController(tty_str='/dev/ttyACM0')

        motor_pin_1 = 32
        AIN_1 = 38
        AIN_2 = 40
        motor_pin_2 = 33
        BIN_1 = 35
        BIN_2 = 37
        LED = 11

        self.c = comunication_module()
        self.c.start_deamon()

        self.old_recv_data = None

        self.motor = Motor(motor_pin_1, motor_pin_2, AIN_1, AIN_2, BIN_1, BIN_2, LED)

        self.current_time = Time()
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.time_speed = 0.01  # ile czasu w sekundach trwa minuta

    def main_loop(self):
        while True:
            print("starto of the loop")
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

                        if self.current_time.m < 10:
                            minute_string = f"0{self.current_time.m}"
                        else:
                            minute_string = f"{self.current_time.m}"

                        current_time_string = f"{self.current_time.d} " + hour_string + minute_string
                        #print(current_time_string)
                        #print(self.pc.rotation.keys())

                        new_recv_data = self.c.recv_data
                        if self.old_recv_data != new_recv_data:
                            self.pc.csv_read_write.which_write(new_recv_data)
                            self.old_recv_data = new_recv_data

                        if current_time_string in self.pc.rotation.keys():
                            print("TEST")
                            print(self.pc.rotation[current_time_string])

                            self.pc.drop_pills(self.pc.rotation[current_time_string])
                            print('Jadymy')
                            self.motor.go()

                        sleep(self.time_speed)


if __name__ == '__main__':
    mr = MainRobot()
    print(mr.pc.csv_read_write.sets)
    print(mr.pc.csv_read_write.pills)
    mr.main_loop()

    # pc = PillController(tty_str='COM5')
    #
    # pc.pill_boxes[5].drop_pill()
    # con = Controller('COM5')
    # print("start")
    # con.setTarget(1, 1500)
